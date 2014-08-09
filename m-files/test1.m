function test1(first,cropXmin,cropYmax,cropXmax,cropYmin,x,y,p1_1,p1_2,p1_3,p1_4,p2_1,p2_2,p2_3,p2_4,p3_1,p3_2,p3_3,p3_4,p4_1,p4_2,p4_3,p4_4)

    first=str2num(first)
    cropXmin=str2num(cropXmin)
    cropYmax=str2num(cropYmax)
    cropXmax=str2num(cropXmax)
    cropYmin=str2num(cropYmin)
    x=str2num(x)
    y=str2num(y)
    
    x1 =[str2num(p1_1), str2num(p2_1),  str2num(p3_1),  str2num(p4_1);
         str2num(p1_2), str2num(p2_2),  str2num(p3_2),  str2num(p4_2);
     1,                  1,                  1,                  1    ]
    
    x2 =[str2num(p1_3), str2num(p2_3),  str2num(p3_3),  str2num(p4_3);
         str2num(p1_4), str2num(p2_4),  str2num(p3_4),  str2num(p4_4);
     1,                 1,                   1,                  1    ]
    
    global cannyMap border junctions
    
    if (first==0)  
 %%%%%%%%%%%%%% read input and crop %%%%%%%%%%%
        [inputMapCrop,c] = imread('C:/matlabPython/SimpleMap.jpg');       %Read image 

        inputMapCrop=inputMapCrop(-cropYmax:-cropYmin,cropXmin:cropXmax,:);
        if c ~= 0                                %Check if c value is greater than zero. If yes the convert it to rgb.
            inputMapCrop = ind2rgb(inputMapCrop,c);
        end
        n = size(inputMapCrop,3);                          
        if(n>1)                                  %Check if image is rgb. If yes convert to gray value.
            inputMapCrop = mat2gray(mean(inputMapCrop,3));
        end
 %%%%%%%%%%%%%% cannyMap %%%%%%%%%%%%%%
        cannyMap=inputMapCrop;
        [a,b] = canny(cannyMap,1);                      %Call canny function
        cannyMap =nonmaxsup(a,b,1.5);                  %Use nonmaxsup on the image obtained from canny
        cannyMap = im2bw(cannyMap,graythresh(cannyMap));
        imwrite(cannyMap,'C:/matlabPython/cannyMap.bmp');
 %%%%%%%%%%%%%%% transform init %%%%%%%%%%%%%%%%%%%  
        h=homo(x1,x2)
        nw=h*[cropXmin;-cropYmax;1]
        ne=h*[cropXmax;-cropYmax;1]
        sw=h*[cropXmin;-cropYmin;1]
        se=h*[cropXmax;-cropYmin;1]
        nw=nw/nw(3)
        ne=ne/ne(3)
        sw=sw/sw(3)
        se=se/se(3)
        cropWidth=cropXmax-cropXmin
        cropHeight=cropYmax-cropYmin
        leftBorder=min(nw(1),sw(1))
        rightBorder=max(ne(1),se(1))
        upperBorder=min(nw(2),ne(2))
        lowerBorder=max(sw(2),se(2))
        tfWidth=max(ne(1),se(1))-min(nw(1),se(1))
        tfHeight=max(nw(2),ne(2))-min(sw(2),se(2))
        tfWdelta=tfWidth/cropWidth
        tfHdelta=tfHeight/cropHeight
        save ('C:/matlabPython/data.mat','tfWdelta','tfHdelta','cropWidth','cropHeight','leftBorder','upperBorder','h')
 %%%%%%%%%%%%%%% transform init %%%%%%%%%%%%%%%%%%% 
        pos=[0;0;1];
        transformedMap=zeros(cropHeight, cropWidth);

        for i=(1:cropHeight)
            pos(2)=upperBorder-i*tfHdelta;
            for j= (1:cropWidth)
                pos(1)=leftBorder+j*tfWdelta;
                proPos=h\pos;
                proPos=proPos/proPos(3);
                transformedMap(i,j)=interpImg(inputMapCrop,[proPos(2)+cropYmax, proPos(1)-cropXmin]);
            end
        end
        imwrite(transformedMap,'C:/matlabPython/transformedMap.bmp');
        
        fileID = fopen('C:/matlabPython/coords.txt','w');
        fprintf(fileID,[num2str(nw(1)),'\n',num2str(nw(2)),'\n',num2str(tfWidth),'\n',num2str(tfHeight)]);
        fclose(fileID);
        
    else
    %%%%%%%%%%%%%%% tracing %%%%%%%%%%%%%%%%%%% 
        load 'C:/matlabPython/data.mat'
        cannyMap = imread('C:/matlabPython/cannyMap.bmp');
        border=zeros(size(cannyMap));
        if(first==1)
            imwrite(border,strcat('C:/matlabPython/border',int2str(0),'.bmp'))
        end
        
        [rj, cj] = findendsjunctions(cannyMap, 0);
        junctions=zeros(size(cannyMap));
        for i=1:length(rj)
            junctions(rj(i),cj(i))=1;
        end
        
        
        stepsToGo=1;
        contourFound=false;
        fileID = fopen('C:/matlabPython/debug0.txt','w');
        fprintf(fileID,[num2str(x),'\n',num2str(y)]);
        fclose(fileID);
        xy=inv(h)*[x;y;1]
        x=xy(1)
        y=xy(2)
        fileID = fopen('C:/matlabPython/debug1.txt','w');
        fprintf(fileID,[num2str(x),'\n',num2str(y)]);
        fclose(fileID);
        y=-y-cropYmax
        x=x-cropXmin
        fileID = fopen('C:/matlabPython/debug2.txt','w');
        fprintf(fileID,[num2str(x),'\n',num2str(y)]);
        fclose(fileID);
        x=round(x);
        y=round(y);
        xnew=0;
        ynew=0;
        if(cannyMap(y,x))
            xnew=x;
            ynew=y;
            contourFound=true;
        else
            while stepsToGo<=21 && contourFound==0%stop at distance of 10(10*2+1)
                for i=1:stepsToGo
                    y=y+1;
                    if (cannyMap(y,x))
                        xnew=x;
                        ynew=y;
                        contourFound=true;
                        break
                    end
                end
                for i=1:stepsToGo
                    x=x+1;
                    if (cannyMap(y,x))
                        xnew=x;
                        ynew=y;
                        contourFound=true;
                        break
                    end
                end
                stepsToGo=stepsToGo+1;
                for i=1:stepsToGo
                    y=y-1;
                    if (cannyMap(y,x))
                        xnew=x;
                        ynew=y;
                        contourFound=true;
                        break
                    end
                end
                for i=1:stepsToGo
                    x=x-1;
                    if (cannyMap(y,x))
                        xnew=x;
                        ynew=y;
                        contourFound=true;
                        break
                    end
                end
                stepsToGo=stepsToGo+1;
            end
        end

        %%%tracing

        if(contourFound)
            set(0,'RecursionLimit',(size(cannyMap,1)+size(cannyMap,2))*2)
            trace(ynew,xnew);
        else
            noPointFoundInRange=10
        end
        border_old = imread(strcat('C:/matlabPython/border',int2str(first-1),'.bmp'));
        for i=1:size(border,1)
            for j=1:size(border,2)
                border(i,j)=or(border(i,j),border_old(i,j));
            end
        end
        imwrite(border,strcat('C:/matlabPython/border',int2str(first),'.bmp'))
        transformedBorder=zeros(cropHeight, cropWidth);
        pos=[0;0;1];
        for i=(1:size(border,1))
            pos(2)=upperBorder-i*tfHdelta;
            for j= (1:size(border,2))
                pos(1)=leftBorder+j*tfWdelta;
                proPos=h\pos;
                proPos=proPos/proPos(3);
                transformedBorder(i,j)=interpImg(border,[proPos(2)+cropYmax, proPos(1)-cropXmin]);
            end
        end
        imwrite(transformedBorder,'C:/matlabPython/transformedMap.bmp');
    end
end


function trace(y,x)
    global cannyMap border junctions
    if~(x<=1 || y<=1 || y>size(cannyMap,1)-1 || x>size(cannyMap,2)-1)
        if junctions(y,x)
            return
        elseif (junctions(y-1,x-1)||junctions(y-1,x)||junctions(y-1,x+1)||junctions(y,x+1)||junctions(y+1,x+1)||junctions(y+1,x)||junctions(y+1,x-1)||junctions(y,x-1))
            junction_pending=true;
        else
            junction_pending=false;
        end
        
        if cannyMap(y-1,x-1)&&~border(y-1,x-1)%NW
            if junction_pending
                if junctions(y-1,x-1)
                    border(y-1,x-1)=1;
                    return
                end
            else
                border(y-1,x-1)=1;
                trace(y-1,x-1);
            end
        end
        
        if cannyMap(y-1,x)&&~border(y-1,x)%N
            if junction_pending
               if junctions(y-1,x)
                    border(y-1,x)=1;
                    return
                end
            else
                border(y-1,x)=1;
                trace(y-1,x);
            end
        end
            
        if cannyMap(y-1,x+1)&&~border(y-1,x+1)%NE
            if junction_pending
                if junctions(y-1,x+1)
                    border(y-1,x+1)=1;
                    return
                end
            else
                border(y-1,x+1)=1;
                trace(y-1,x+1);
            end
        end

        if cannyMap(y,x+1)&&~border(y,x+1)%E
            if junction_pending
                if junctions(y,x+1)
                    border(y,x+1)=1;
                    return
                end
            else
                border(y,x+1)=1;
                trace(y,x+1);
            end
        end

        if cannyMap(y+1,x+1)&&~border(y+1,x+1)%SE
            if junction_pending
                if junctions(y+1,x+1)
                    border(y+1,x+1)=1;
                    return
                end
            else
                border(y+1,x+1)=1;
                trace(y+1,x+1);
            end
        end

        if cannyMap(y+1,x)&&~border(y+1,x)%S
            if junction_pending
                if junctions(y+1,x)
                    border(y+1,x)=1;
                    return
                end
            else
                border(y+1,x)=1;
                trace(y+1,x);
            end
        end

        if cannyMap(y+1,x-1)&&~border(y+1,x-1)%SW
            if junction_pending
                if junctions(y+1,x-1)
                    border(y+1,x-1)=1;
                    return
                end
            else
                border(y+1,x-1)=1;
                trace(y+1,x-1);
            end
        end

        if cannyMap(y,x-1)&&~border(y,x-1)%W
            if junction_pending
                if junctions(y,x-1)
                    border(y,x-1)=1;
                    return
                end
            else
                border(y,x-1)=1;
                trace(y,x-1);
            end
        end
    end
end