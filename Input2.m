
%�����ļ�˵��

%ά��(ndim)�� �ܽ����(nnode)��  �˵�Ԫ��Ŀ��   ��������Ԫ��(nelem_cable)��  Cluster����Ԫ��(nelem_1)
ndim=3;       nnode=12;        nelem_bar=2;      nelem_cable=3;            nelem_cluster=1;
mdof=ndim*nnode;

%Cluster����m*n��: m--cluster�ĸ���; n--ÿ��cluster���еľ��䵥Ԫ��Ŀ
cluster=[1,2,3,4,5,6];
mn=size(cluster);
m=mn(1,1);n=mn(1,2);

%��Ԫ��ŷ�Ϊ���ࣺ�˵�Ԫ����������Ԫ��Cluster����Ԫ
ele_bar=[3,8;...
         5,9];

ele_cable=[2,10;...
           4,11;...
           6,12];

ele_cluster=[1,2;...
             2,3;...
             3,4;...
             4,5;...
             5,6;...
             6,7];

%��Ԫ���ϲ����������������ģ������Ӧ�䣬��Ӧ����
a_cable=0.5e-4;
a_bar=2.8e-4;
a_cluster=1e-4;

e_bar=2e11;
e_cable=1e11;
e_cluster=1e11;

%�ڵ�����
nod=[0,0,0;...
    1,0.5,0;...
    2,0,0;...
    3,0.5,0;...
    4,0,0;...
    5,0.5,0;...
    6,0,0;...
    2,-1.5,0;...
    4,-1.5,0;...
    1,1.5,0;...
    3,1.5,0;...
    5,1.5,0];

%Լ��x��λ�ƵĽڵ㣬Լ��y��λ�ƵĽڵ㣬Լ��z��λ�ƵĽڵ�
lrx=[1,7,8,9,10,11,12];
lry=[1,7,8,9,10,11,12];
lrz=[1,2,3,4,5,6,7,8,9,10,11,12];

xxx=size(lrx);yyy=size(lry);zzz=size(lrz);
nrx=xxx(1,2);nry=yyy(1,2);nrz=zzz(1,2);

%�غ���Ϣ���ܼ��ز��������ز���
f=zeros(mdof,1);
f(ndim*4-2,1)=0;

%===============================Initial====================================
nod_now=zeros(nnode,3);nod_delta=zeros(nnode,3);
dis0=zeros(mdof,1);dis1=zeros(mdof,1);delta_dis=zeros(mdof,1);
q=zeros(mdof,1);df=zeros(mdof,1);
kte_bar=zeros(6,6);kte_cable=zeros(6,6);kte_cluster=zeros(3*(n+1),3*(n+1));
Kt=zeros(mdof,mdof);





