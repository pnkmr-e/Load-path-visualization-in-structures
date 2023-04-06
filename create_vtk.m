clear
close all
clc

fileId1 = fopen('Plate_with_hole_distributed.vtk','w'); %open file for writing; discard existing contents
fprintf(fileId1,'# vtk DataFile Version 2.0 \n');
fprintf(fileId1,'Unstructured Grid - Plate with hole 2D \n');

%read data
nlist = readtable('NLIST.txt'); % get the locations of the nodes
u_star = readtable('U_STAR.txt'); % U* data % 'Delimiter',' ','MultipleDelimsAsOne', true
etable = readtable('ELIST.txt'); % get the element-nodes connectivity
element_type = fgets(fopen('element_type.txt'));
element_type = str2num(element_type(9:end));

%convert it to array
nlist = table2array(nlist);
u_star = table2array(u_star);
etable = int64(table2array(etable));
etable(:,2:6) = []; %removing useless columns from ELIST
nodes_per_element = length(etable(1,:))-1 ;

etable(:,all(etable == 0))=[]; % remove all the zero columns
etable=etable-1; % because the indexing in paraview starts from 0 not from 1
etable_vtk = etable ;
etable_vtk(:,1) = nodes_per_element; % insert the number of nodes for element in the first column

if  element_type == 181 || element_type == 182
    cell_type = 9;
elseif element_type == 183
    cell_type = 23;
elseif element_type == 185
    cell_type = 12;
elseif element_type == 186
    cell_type = 25;
elseif element_type == 187
    cell_type = 24;    
end
% if nodes_per_element == 20
%     cell_type = 25;
% end
%%


fprintf(fileId1,'ASCII \n');
fprintf(fileId1,'DATASET UNSTRUCTURED_GRID \n');
% Define points
fprintf(fileId1,'\nPOINTS %d float \n', length(nlist(:,1)));
for i =1 :length(nlist(:,1))
    fprintf(fileId1,'%d ',nlist(i,[2:4]));
    fprintf(fileId1,'\n ');
end
% define cells
fprintf(fileId1,'\nCELLS %d %d \n', length(etable(:,1)), size(etable,1)*size(etable,2));

for i =1 :length(etable_vtk(:,1))
    fprintf(fileId1, '%d ', etable_vtk(i,:));   % order is changed because of the format
    fprintf(fileId1,'\n ');
end
%%
% define cell data
fprintf(fileId1,'\nCELL_TYPES %d \n',length(etable(:,1)));
for i =1 :length(etable(:,1))
    fprintf(fileId1,'%d \n', cell_type );
end

fprintf(fileId1,'POINT_DATA %d \n',length(nlist(:,1)));
fprintf(fileId1,'SCALARS U_star float 1 \n');
fprintf(fileId1,'LOOKUP_TABLE default \n');
for i= 1:length(nlist(:,1))
    fprintf(fileId1,'%d \n', u_star(i,2) );
end

figure
plot3(nlist(:,2),nlist(:,3),nlist(:,4),'*')
hold on
% text(nlist(:,2),nlist(:,3),nlist(:,4),string(nlist(:,1)))
% axis equal