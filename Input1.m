
%输入文件说明

%维数(ndim)， 总结点数(nnode)，  杆单元数目，   经典绳单元数(nelem_cable)，  Cluster绳单元数(nelem_1)
ndim=3;       nnode=3;        nelem_bar=0;      nelem_cable=0;   nelem_spring=0;         nelem_cluster=1;
mdof=ndim*nnode;

%Cluster矩阵（m*n）: m--cluster的根数; n--每根cluster含有的经典单元数目
cluster=[1,2];
mn=size(cluster);
m=mn(1,1);n=mn(1,2);


%单元编号分为三类：杆单元，经典绳单元，Cluster绳单元
ele_bar=[];

ele_cable=[0,0];

ele_cluster=[1,2;...
             2,3];
         
         
ele_spring=[];         

%单元材料参数（截面积，弹性模量，初应变，初应力）
a_cable=1;
a_bar=1;
a_cluster=1;

e_bar=2e4;
e_cable=2e4;
e_cluster=2e4;
stiff_spring1=0;
stiff_spring2=0;

%节点坐标
nod=[0,0,0;...
     1,1,0;...
     2,0,0];

%约束x向位移的节点，约束y向位移的节点，约束z向位移的节点
lrx=[1,3];
lry=[1,3];
lrz=[1,2,3];

xxx=size(lrx);yyy=size(lry);zzz=size(lrz);
nrx=xxx(1,2);nry=yyy(1,2);nrz=zzz(1,2);


delta_spring0=zeros(nelem_spring,1);
delta_bar0=zeros(nelem_bar,1);
delta_cable0=zeros(nelem_cable,1);
delta_cluster0=zeros(nelem_cluster,1);

%载荷信息，总加载步数，加载步长
f=zeros(mdof,1);


%===============================Initial====================================
nod_now=zeros(nnode,3);nod_delta=zeros(nnode,3);
dis0=zeros(mdof,1);dis1=zeros(mdof,1);delta_dis=zeros(mdof,1);
q=zeros(mdof,1);df=zeros(mdof,1);
kte_bar=zeros(6,6);kte_cable=zeros(6,6);kte_cluster=zeros(3*(n+1),3*(n+1));
Kt=zeros(mdof,mdof);





