
%�����ļ�˵��

%ά��(ndim)�� �ܽ����(nnode)��  �˵�Ԫ��Ŀ��   ��������Ԫ��(nelem_cable)�� ���ɵ�Ԫ��(nelem_1),   Cluster����Ԫ��(nelem_1)
ndim=3;       nnode=12;         nelem_bar=8;      nelem_cable=8;         nelem_spring=4;          nelem_cluster=4;
mdof=ndim*nnode;

%Cluster����m*n��: m--cluster�ĸ���; n--ÿ��cluster���еľ��䵥Ԫ��Ŀ
cluster=[1,2;...
         3,4;...
         5,6;...
         7,8];
     
     
mn=size(cluster);
m=mn(1,1);n=mn(1,2);


%��Ԫ��ŷ�Ϊ���ࣺ�˵�Ԫ����������Ԫ��cluster����Ԫ
ele_bar=[1,6;2,7;3,8;4,5;...
         5,11;6,12;7,9;8,10];

ele_cable=[1,2;2,3;3,4;4,1;...
           9,10;10,11;11,12;12,9;...
           ];

ele_cluster=[9,8;8,4;...
             1,5;5,10;...
             3,7;7,12;...
             2,6;6,11];

ele_spring=[5,8;5,6;6,7;7,8];


%��Ԫ���ϲ����������������ģ������Ӧ�䣬��Ӧ����
a_cable=0.5026;
a_bar=2.55;
a_cluster=0.5026;

e_bar=7000;
e_cable=11500;
e_cluster=11500;
stiff_spring=1;

%�ڵ�����
nod=[0,0,0;...
     80,0,0;...
     80,80,0;...
     0,80,0;...
     40,0,40;...
     80,40,40;...
     40,80,40;...
     0,40,40;...
     0,0,80;...
     80,0,80;...
     80,80,80;...
     0,80,80];


%��ʼ�쳤��
delta_spring0=zeros(nelem_spring,1);
delta_bar0=zeros(nelem_bar,1);
delta_cable0=zeros(nelem_cable,1);
delta_cluster0=zeros(nelem_cluster,1);


%Լ��x��λ�ƵĽڵ㣬Լ��y��λ�ƵĽڵ㣬Լ��z��λ�ƵĽڵ�
lrx=[1];
lry=[1,2];
lrz=[1,2,3,4];

xxx=size(lrx);yyy=size(lry);zzz=size(lrz);
nrx=xxx(1,2);nry=yyy(1,2);nrz=zzz(1,2);

%�غ���Ϣ���ܼ��ز��������ز���
f=zeros(mdof,1);


%===============================Initial====================================
nod_now=zeros(nnode,3);nod_delta=zeros(nnode,3);
dis0=zeros(mdof,1);dis1=zeros(mdof,1);delta_dis=zeros(mdof,1);
q=zeros(mdof,1);df=zeros(mdof,1);
kte_bar=zeros(6,6);kte_cable=zeros(6,6);kte_cluster=zeros(3*(n+1),3*(n+1));
Kt=zeros(mdof,mdof);





