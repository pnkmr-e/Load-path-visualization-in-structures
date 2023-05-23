close all
clear
clc

M = dlmread('principal_streamline_82.csv',',',1,1);
XYZ = M(:,9:11);
Ustar = M(:,13);

lengthInc = zeros(length(XYZ),1);
lengthInc(2:end) = sqrt( sum( (XYZ(2:end,:)-XYZ(1:end-1,:)).^2 ,2) );
streamlineCoord = zeros(size(lengthInc));
for i=1:length(streamlineCoord)
    streamlineCoord(i) = sum(lengthInc(1:i));
end

s = streamlineCoord/streamlineCoord(end); %normalised streamline coordinate

%% Polynomial fitting
% Making a sufficient order polynomial fit for curvature values
p = polyfit(s,Ustar,12);
sfit = linspace(0,1,101);
Ustarfit = polyval(p,sfit);


%% Uniformity plot
fig1 = figure(1);
% yyaxis left
plot(sfit,Ustarfit,'-b','LineWidth',1.4)
ylim([0,1])

hold on
plot([0,1],[0,1],'-k','LineWidth',0.1)

set(gca,'FontSize',12)
fig1.Units = 'centimeters';
fig1.Position(3:4) = [12 8];
grid on
grid minor
title('\textbf{Uniformity curve}', 'FontSize',14, 'Interpreter','latex')
xlabel('\textbf{s}', 'FontSize',12, 'Interpreter','latex')
ylabel('\textbf{U*}', 'FontSize',12, 'Interpreter','latex')


%% Continuity plot

%-----------------------------
%%% ALSO WORKS %%%
% dydx  = gradient(y,x);
% d2ydx2 = gradient(dy,x);
% num   = d2ydx2;
% denom = ( 1+dydx.^2 ).^(3/2)
%-----------------------------

ds  = gradient(sfit);
dds = gradient(ds);
dy  = gradient(Ustarfit);
ddy = gradient(dy);
num   = ds .* ddy - dds .* dy;
denom = ds .* ds + dy .* dy;
denom = denom.^(3/2);
curvUstar = num ./ denom;
% curvUstar(denom < 0) = NaN;

% figure(1)
fig2 = figure(2);
% yyaxis right
plot(sfit,curvUstar,'-r','LineWidth',1.4)
ylim([-10 10])

hold on
plot([0,1],[0,0],'-k','LineWidth',0.1)

set(gca,'FontSize',12)
fig2.Units = 'centimeters';
fig2.Position(3:4) = [12 8];
grid on
grid minor
title('\textbf{Continuity curve}', 'FontSize',14, 'Interpreter','latex')
xlabel('\textbf{s}', 'FontSize',12, 'Interpreter','latex')
ylabel('\textbf{Curvature}', 'FontSize',12, 'Interpreter','latex')

