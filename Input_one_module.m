
%�����ļ�˵��

%ά��(ndim)�� �ܽ����(nnode)��  �˵�Ԫ��Ŀ��   ��������Ԫ��(nelem_cable)��  Cluster����Ԫ��(nelem_1)
ndim=3;       nnode=8;        nelem_bar=4;      nelem_cable=12;   nelem_spring=0;         nelem_cluster=0;
mdof=ndim*nnode;

%Cluster����m*n��: m--cluster�ĸ���; n--ÿ��cluster���еľ��䵥Ԫ��Ŀ
cluster=[];
mn=size(cluster);
m=mn(1,1);n=mn(1,2);


%��Ԫ��ŷ�Ϊ���ࣺ�˵�Ԫ����������Ԫ��Cluster����Ԫ
ele_bar=[1,5;...
         2,8;...
         3,6;...
         4,7];

ele_cable=[1,6;...
             2,7;...
             1,2;...
             6,7;...
             3,4;...
             3,5;...
             4,8;...
             5,8;...
             2,5;...
             7,8;...
             4,6;...
             1,3;];

ele_cluster=[];
         
         
ele_spring=[];         

%%%%%%%%%%��Ӧ��
delta_T=200;           %Ŀǰ��������¶�
ele_num_temp1=[1;2];   %�����
alpha=30e-6;              %Ŀǰ�������������ϵ��
delta_T_temp0=zeros(nelem_cable,1);
delta_T_temp1=delta_T_temp0;
for i=1:numel(ele_num_temp1)

delta_T_temp1(ele_num_temp1(i))=delta_T;

end

epsilon_cable_temp1=alpha*delta_T_temp1;
%%%%%%%%%%%%%%%%%%%%%%%%%%


%��Ԫ���ϲ����������������ģ������Ӧ�䣬��Ӧ����
a_cable=0.28e-4;
a_bar=0.325e-4;
a_cluster=0;

e_bar=200e9;
e_cable=40e9;e_cable_com=0;
e_cluster=0;
stiff_spring1=0;
stiff_spring2=0;

%�ڵ�����
nod=[0,0,0;...
     0,1,0;...
     0,0.5,0.5;...
     0.5,0,0.5;...
     0.5,1,0.5;...
     1,0,0;...
     1,1,0;...
     1,0.5,0.5];

%  nod=[
%                           0                         0                         0;...
%                          0    1.000000000000000e+000    3.089655417372176e-016;...
%                          0    4.999538226290243e-001    4.998841964185526e-001;...
%     4.998988342800447e-001    1.463125422301114e-005    4.998469564337176e-001;...
%     4.999161440348518e-001    9.998757536426275e-001    4.999217526804375e-001;...
%     9.998845162359153e-001    2.306820000855390e-005   -5.386288686198826e-006;...
%     9.998845118224733e-001    9.999076357205571e-001    2.925525373055033e-005;...
%     9.998149175267816e-001    4.999365005843449e-001    4.998960707222699e-001];

%Լ��x��λ�ƵĽڵ㣬Լ��y��λ�ƵĽڵ㣬Լ��z��λ�ƵĽڵ�
lrx=[1,2,3];
lry=[1,2];
lrz=[1];

xxx=size(lrx);yyy=size(lry);zzz=size(lrz);
nrx=xxx(1,2);nry=yyy(1,2);nrz=zzz(1,2);




%========================================����Ӧ��
delta_spring0=zeros(nelem_spring,1);
delta_bar0=zeros(nelem_bar,1);
delta_cable0=zeros(nelem_cable,1);
delta_cluster0=zeros(nelem_cluster,1);

FF(1:4,1)=5.5e3;
FF(5:8,1)=7.7782e3;
FF(9:12,1)=7.84440e3;
FF(13:16,1)=-1.34722e4;

LL(1:4,1)=100e-2;
LL(5:12,1)=70.71067811865476e-2;
LL(13:16,1)=122.4744871391589e-2;


for i=1:12
    LL0(i,1)= LL(i,1)*(e_cable*a_cable-FF(i,1))/(e_cable*a_cable);
end

for i=13:16
   LL0(i,1)= LL(i,1)*(e_bar*a_bar-FF(i,1))/(e_bar*a_bar);
end

delta_cable0(:,1)=LL(1:12)-LL0(1:12);
delta_bar0(:,1)=LL(13:16)-LL0(13:16);
%=============================================�غ���Ϣ���ܼ��ز��������ز���
f=zeros(mdof,1);


%===============================Initial====================================
nod_now=zeros(nnode,3);nod_delta=zeros(nnode,3);
dis0=zeros(mdof,1);dis1=zeros(mdof,1);delta_dis=zeros(mdof,1);
q=zeros(mdof,1);df=zeros(mdof,1);
kte_bar=zeros(6,6);kte_cable=zeros(6,6);kte_cluster=zeros(3*(n+1),3*(n+1));
Kt=zeros(mdof,mdof);





