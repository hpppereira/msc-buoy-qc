% =============================================================
%              PROJETO BACIA ES
% =============================================================
% ler os arquivos da boia do ES
% coordenadas: lat 19.57'
%              lon 39°32'
% intervalo de dados: 1 hora
% inicio:2006-10-12 00h
% final: 2007-01-15 23h
% =============================================================
close all
clc
clear all

work='/home/izabel/Projetos/Espirito_Santo/rodada/teste_hindcasting/200610';
% ----------- MEDIDO ----------------------------
saida=load('saida.out');
% --
dia=saida(:,1);mes=saida(:,2);ano=saida(:,3);hora=saida(:,4);min=saida(:,5);
% --
% altura significativa
hs=4.*sqrt(saida(1:1801,17));
% periodo de pico
tp=saida(1:1801,22);
%direcao de pico
dp=saida(1:1801,26);

fid = fopen('DADOSBOIA.txt', 'w');
for i=1:length(hs);
    fprintf(fid,'%6.2f %6.2f %6.2f\r\n', hs(i),tp(i),dp(i));
end
fclose(fid);


% conhecendo os dados
% ............... MEDIDAS DE TENDÊNCIA CENTRAL ...................
disp('média')
mean(hs)
mean(tp)
mean(dp)
disp('desvio')
std(hs)
std(tp)
std(dp)
% .................... PERCENTIL..................................
disp('percentil, 0% 90% 100%')
prctile(hs, [0, 90, 100])
prctile(tp, [0, 90, 100])
prctile(dp, [0, 90, 100])

%                       HS vs. TP
class{1}=1:2:21;class{2}=0.25:0.5:5.25;
%xb=class{1};yb=class{2};
X = [tp,hs];n=hist3(X,class);n1 = ((n'.*100)/length(hs)); 
n1( size(n,2) + 1 ,size(n,1) + 1 ) = 0; 
xb = linspace(1,22,size(n,1)+1);
yb = linspace(0.25,5.75,size(n,2)+1);

figure1=figure(1);
clear axes1
axes1=axes('Parent',figure1,'FontSize',16,'FontWeight','b');
hold(axes1,'all');box(axes1,'on');grid(axes1,'on');
[C h]=contour(xb,yb,n1,15,'LineWidth',1.5);grid on
for a=1:length(n(:,1));
    for b=1:length(n(1,:));
        if (n(a,b)>0);
            label=num2str(n(a,b));
            text(xb(a),yb(b),label,'fontsize',14,'fontweight','b');
        end
    end
end
ylabel('Altura Significativa (m)','fontsize',19,'FontWeight','b')
xlabel('Período de Pico (s)','fontsize',19,'FontWeight','b')
cm=colorbar('FontWeight','bold','FontSize',16);
set(get(cm,'ylabel'),'String', 'Porcentagem de Ocorrência (%)',...
    'fontsize',18);
text(max(max(xb))-4,max(max(yb))-4,num2str(length(hs)),'fontsize',18);
text(max(max(xb))-4,max(max(yb))-4,'N_{total}: ','fontsize',18);
ylim([0 5]);xlim([0 22])

%                    HS vs, DP
clear n n1 xb yb X class axes1
class{1}=0:45:360;class{2}=0.25:0.5:5.25;
%xb=class{1};yb=class{2};
X = [dp,hs];n = hist3(X,class); 
n1 = ((n'.*100)/length(hs)); 
n1( size(n,2) + 1 ,size(n,1) + 1 ) = 0; 
xb = linspace(0,405,size(n,1)+1);
yb = linspace(0.25,5.75,size(n,2)+1);

figure2=figure(2);
axes1=axes('Parent',figure2,'FontSize',16,'FontWeight','b',...
    'XTickLabel',{'N','NE','E','SE','S','SW','W'},...
    'XTick',[0 45 90 135 180 225 270]);
hold(axes1,'all');box(axes1,'on');grid(axes1,'on');    
[C h]=contour(xb,yb,n1,15,'LineWidth',1.5);grid on
for a=1:length(n(:,1));
    for b=1:length(n(1,:));
        if (n(a,b)>0);
            label=num2str(n(a,b));
            text(xb(a),yb(b),label,'fontsize',14,'fontweight','b');
        end
    end
end
ylabel('Altura Significativa (m)','fontsize',19,'FontWeight','b')
xlabel('Direção de Pico (°)','fontsize',19,'FontWeight','b')
cm=colorbar('FontWeight','bold','FontSize',16);
set(get(cm,'ylabel'),'String', 'Porcentagem de Ocorrência (%)',...
    'fontsize',18);
text(max(max(xb))-190,max(max(yb))-4,num2str(length(hs)),'fontsize',18);
text(max(max(xb))-190,max(max(yb))-4,'N_{total}: ','fontsize',18);
ylim([0 5]);xlim([0 270])

%                TP vs. DP
clear n1 n xb yb X class axes1
class{1}=0:45:360;class{2}=1:2:21;
%xb=class{1};yb=class{2};
X = [dp,tp];n = hist3(X,class);
n1 = ((n'.*100)/length(hs)); 
n1( size(n,2) + 1 ,size(n,1) + 1 ) = 0; 
xb = linspace(0,405,size(n,1)+1);
yb = linspace(1,22,size(n,2)+1);

figure3=figure(3);
axes1=axes('Parent',figure3,'FontSize',16,'FontWeight','b',...
    'XTickLabel',{'N','NE','E','SE','S','SW','W'},...
    'XTick',[0 45 90 135 180 225 270]);
hold(axes1,'all');box(axes1,'on');grid(axes1,'on');
[C h]=contour(xb,yb,n1,15,'LineWidth',1.5);grid on
for a=1:length(n(:,1));
    for b=1:length(n(1,:));
        if (n(a,b)>0);
            label=num2str(n(a,b));
            text(xb(a),yb(b),label,'fontsize',14,'fontweight','b');
        end
    end
end
ylabel('Período de Pico (s)','fontsize',19,'FontWeight','b')
xlabel('Direção de Pico (°)','fontsize',19,'FontWeight','b')
cm=colorbar('FontWeight','bold','FontSize',16);
set(get(cm,'ylabel'),'String', 'Porcentagem de Ocorrência (%)',...
    'fontsize',18);
text(max(max(xb))-190,max(max(yb))-10,num2str(length(hs)),'fontsize',18);
text(max(max(xb))-190,max(max(yb))-10,'N_{total}: ','fontsize',18);
xlim([0 270]);
ylim([0 22]);



% --------------- MODELADO --------------------------
modelo=load('grade10.tab'); % rodada do hindcast
hs_mod10=modelo(265:744,5);
%direcao de pico
dp_mod10=modelo(265:744,11);
% frequencia de pico
fp_mod10=modelo(265:744,10);
% periodo de pico
tp_mod10(:,1)=1./fp_mod10;

clear modelo
modelo=load('grade11.tab'); % rodada do hindcast
hs_mod11=modelo(:,5);
%direcao de pico
dp_mod11=modelo(:,11);
% frequencia de pico
fp_mod11=modelo(:,10);
% periodo de pico
tp_mod11(:,1)=1./fp_mod11;

clear modelo
modelo=load('grade12.tab'); % rodada do hindcast
hs_mod12=modelo(1:600,5);
%direcao de pico
dp_mod12=modelo(1:600,11);
% frequencia de pico
fp_mod12=modelo(1:600,10);
% periodo de pico
tp_mod12(:,1)=1./fp_mod12;

hs_mod=[hs_mod10;hs_mod11;hs_mod12];
dp_mod=[dp_mod10;dp_mod11;dp_mod12];
tp_mod=[tp_mod10;tp_mod11;tp_mod12];

% conhecendo os dados
% ............... MEDIDAS DE TENDÊNCIA CENTRAL ...................
disp('média modelo')
mean(hs_mod)
mean(tp_mod)
mean(dp_mod)
disp('desvio')
std(hs_mod)
std(tp_mod)
std(dp_mod)
% .................... PERCENTIL..................................
disp('percentil, 0% 90% 100%')
prctile(hs_mod, [0, 90, 100])
prctile(tp_mod, [0, 90, 100])
prctile(dp_mod, [0, 90, 100])


% ===========================================================
%                 PLOTAR RESULTADOS
% ===========================================================
datain=datenum(2006,10,12,00,00,00);%dia inicial da coleta (YY,MM,DD,HH,MM,SS)
datafi=datenum(2006,12,25,23,00,00);% dia final
tempos=linspace(datain,datafi,1801);
tempos1=tempos(1:120:end);
%tempos=linspace(datain,datafi,str2num(datestr(datafi(end),7))); %coloca o eixo espaçado em dias

% Altura Significativa 
figure1=figure(1);
subplot1 = subplot(3,1,1,'Parent',figure1,...
    'YTick',[0 1 2 3 4 5],...
    'FontWeight','bold',...
    'FontSize',16);
box(subplot1,'on');
grid(subplot1,'on');
hold(subplot1,'all');
plot(tempos,hs,'--bx','LineWidth',2); hold on
plot(tempos,hs_mod,'--kx','LineWidth',2)
set(gca,'xtick',tempos1);
set(gca,'xticklabel',datestr(tempos1,19));
%title('Altura Significativa','FontWeight','Bold','fontsize', 16)
ylim ([0 5])
%xlabel('data','fontsize',12,'fontweight','b')
ylabel('Hs (m)','fontsize',18,'fontweight','b')
h = legend('Observado','Modelado',4);
set(h,'Interpreter','none','Orientation','horizontal',...
    'fontsize',18,'fontweight','b','linewidth',3)


% Periodo de pico
subplot1 = subplot(3,1,2,'Parent',figure1,...
    'YTick',[0 5 10 15 20],...
    'FontWeight','bold',...
    'FontSize',16);
box(subplot1,'on');
grid(subplot1,'on');
hold(subplot1,'all');
plot(tempos,tp,'--bx','LineWidth',2);hold on
plot(tempos,tp_mod,'--kx','LineWidth',2)
set(gca,'xtick',tempos1);
set(gca,'xticklabel',datestr(tempos1,19));
%title('Período Médio','FontWeight','Bold','fontsize', 16)
ylim ([0 20])
%xlabel('Registro','fontsize',12,'fontweight','b')
ylabel('Tp (s)','fontsize',18,'fontweight','b')
grid on

% Direcao de pico
subplot1 = subplot(3,1,3,'Parent',figure1,...
    'YTick',[0 90 180 270 360],...
    'FontWeight','bold',...
    'FontSize',16);
box(subplot1,'on');
grid(subplot1,'on');
hold(subplot1,'all');
plot(tempos,dp,'--bx','LineWidth',2);hold on
plot(tempos,dp_mod,'--kx','LineWidth',2)
set(gca,'xtick',tempos1);
set(gca,'xticklabel',datestr(tempos1,19));
%title('Direção Média','FontWeight','Bold','fontsize', 16)
%xlabel('Data','fontsize',12,'fontweight','b')
ylabel('Dp (°)','fontsize',18,'fontweight','b')
ylim([0 360])
grid on

% Altura significativa
%media
% Correlacao
Correlacao = corr(hs,hs_mod)
% Vicio (BIAS)
bias=mean(hs_mod-hs) 
% Erro quadratico medio:
l=length(hs);
rmse = sqrt( sum( (hs_mod(:)-hs(:)).^2) / l )
mdobs = mean(hs);
% Índice de Espalhamento
SI= rmse/mdobs
desv=std(hs)

disp('periodo de pico')
% Correlacao
Correlacao = corr(tp_mod,tp)
% Vicio (BIAS)
bias=mean(tp_mod-tp) 
% Erro quadratico medio:
l=length(tp);
rmse = sqrt( sum( (tp_mod(:)-tp(:)).^2) / l )
mdobs = mean(tp);
% Índice de Espalhamento
SI= rmse/mdobs
desv=std(tp)

disp('direcao de pico')
% Correlacao
Correlacao = corr(dp_mod,dp)
% Vicio (BIAS)
bias=mean(dp_mod-dp) 
% Erro quadratico medio:
l=length(dp);
rmse = sqrt( sum( (dp_mod(:)-dp(:)).^2) / l )
mdobs = mean(dp);
% Índice de Espalhamento
SI= rmse/mdobs
desv=std(dp)

figure2=figure(2);
y=hs_mod;x=hs;
subplot1 = subplot(1,3,1,'Parent',figure2,...
    'FontWeight','bold',...
    'FontSize',16,'LineWidth',1,'GridLineStyle','--');
box(subplot1,'on');
grid(subplot1,'on');
hold(subplot1,'all');
plot(x, y, 'ko','MarkerFaceColor',[0.5 0.5 0.5]);hold on
plot((0:5),(0:5),'k','LineWidth',2)
h=lsline;
xlabel('Hs Observado','fontsize',18,'fontweight','b');
ylabel('Hs Modelado','fontsize',18,'fontweight','b')
axis([0 5 0 5])
 text(4.5, 0.2, ['r = ' num2str(corr(x,y))],...
     'fontsize',14,'fontweight','b')

y=tp_mod;x=tp;
subplot1 = subplot(1,3,2,'Parent',figure2,...
    'FontWeight','bold',...
    'FontSize',16,'LineWidth',1,'GridLineStyle','--');
box(subplot1,'on');
grid(subplot1,'on');
hold(subplot1,'all');
plot(x, y, 'ko','MarkerFaceColor',[0.5 0.5 0.5]);hold on
plot((0:18),(0:18),'k','LineWidth',2)
h=lsline;
xlabel('Tp Observado','fontsize',18,'fontweight','b');
ylabel('Tp Modelado','fontsize',18,'fontweight','b')
axis([0 18 0 18])
 text(4.5, 0.2, ['r = ' num2str(corr(x,y))],...
     'fontsize',14,'fontweight','b')
 
 y=dp_mod;x=dp;
subplot1 = subplot(1,3,3,'Parent',figure2,...
    'FontWeight','bold',...
    'FontSize',16,'LineWidth',1,'GridLineStyle','--');
box(subplot1,'on');
grid(subplot1,'on');
hold(subplot1,'all');
plot(x, y, 'ko','MarkerFaceColor',[0.5 0.5 0.5]);hold on
plot((0:360),(0:360),'k','LineWidth',2)
h=lsline;
xlabel('Dp Observado','fontsize',18,'fontweight','b');
ylabel('Dp Modelado','fontsize',18,'fontweight','b')
axis([0 360 0 360])
 text(280, 10, ['r = ' num2str(corr(x,y))],...
     'fontsize',14,'fontweight','b')