
%�����ļ�˵��

%ά��(ndim)�� �ܽ����(nnode)��  �˵�Ԫ��Ŀ��   ��������Ԫ��(nelem_cable)��  Cluster����Ԫ��(nelem_1)
ndim=3;       nnode=8;         nelem_bar=4;      nelem_cable=16;            nelem_cluster=0;
mdof=ndim*nnode;

%Cluster����m*n��: m--cluster�ĸ���; n--ÿ��cluster���еľ��䵥Ԫ��Ŀ
cluster=[];
     
     
mn=size(cluster);
m=mn(1,1);n=mn(1,2);


%��Ԫ��ŷ�Ϊ���ࣺ�˵�Ԫ����������Ԫ��Cluster����Ԫ
ele_bar=[1,8;2,6;3,7;4,5];

ele_cable=[1,2;1,3;2,4;3,4;5,6;5,7;6,8;7,8;1,5;1,6;2,5;2,7;3,6;3,8;4,7;4,8];

ele_cluster=[5,14;7,14;2,11;4,11;...
             7,14;7,16;2,9;2,11;13,22;15,22;10,19;12,19;...
             15,22;15,24;10,17;10,19];

%��Ԫ���ϲ����������������ģ������Ӧ�䣬��Ӧ����
a_cable=1;
a_bar=1;
a_cluster=1;

e_bar=2e4;
e_cable=2e4;
e_cluster=2e4;

%�ڵ�����
nod=[26.67,80,0;80,53.34,0;0,26.67,0;53.34,0,0;53.34,80,30;0,53.34,30;80,26.67,30;26.67,0,30];

%Լ��x��λ�ƵĽڵ㣬Լ��y��λ�ƵĽڵ㣬Լ��z��λ�ƵĽڵ�
lrx=[1,3,6];
lry=[1,3,6];
lrz=[1,3,6];

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





