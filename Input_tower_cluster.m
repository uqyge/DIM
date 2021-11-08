
%�����ļ�˵��

%ά��(ndim)�� �ܽ����(nnode)��  �˵�Ԫ��Ŀ��   ��������Ԫ��(nelem_cable)��  Cluster����Ԫ��(nelem_1)
ndim=3;       nnode=20;         nelem_bar=16;      nelem_cable=8;       nelem_spring=12;     nelem_cluster=4;
mdof=ndim*nnode;

%Cluster����m*n��: m--cluster�ĸ���; n--ÿ��cluster���еľ��䵥Ԫ��Ŀ
cluster=[1,2,3,4;...
         5,6,7,8;...
         9,10,11,12;...
         13,14,15,16];
     
     
mn=size(cluster);
m=mn(1,1);n=mn(1,2);


%��Ԫ��ŷ�Ϊ���ࣺ�˵�Ԫ����������Ԫ��cluster����Ԫ
ele_spring=[5,6;6,7;7,8;8,5;...
            9,10;10,11;11,12;12,9;...
            13,14;14,15;15,16;16,13;...
            ];

ele_bar=[1,6;2,7;3,8;4,5;...
         5,11;6,12;7,9;8,10;...
         9,14;10,15;11,16;12,13;...
         13,19;14,20;15,17;16,18];

ele_cable=[1,2;2,3;3,4;1,4;...
           17,18;18,19;19,20;17,20];

ele_cluster=[1,5;5,10;10,14;14,19;...
             2,6;6,11;11,15;15,20;...
             3,7;7,12;12,16;16,17;...
             4,8;8,9;9,13;13,18];

%��Ԫ���ϲ����������������ģ������Ӧ�䣬��Ӧ����
a_cable=0.5026;
a_bar=2.55;
a_cluster=0.5026;

stiff_spring1=0.2;
stiff_spring2=5;

e_bar=7000;
e_cable=11500;
e_cluster=11500;



nod=100*[0,0,0
1,0,0
1,1,0
0,1,0
0.5,0,0.5
1,0.5,0.5
0.5,1,0.5
0,0.5,0.5
0,0,1
1,0,1
1,1,1
0,1,1
0.5,0,1.5
1,0.5,1.5
0.5,1,1.5
0,0.5,1.5
0,0,2
1,0,2
1,1,2
0,1,2];


% nod=100*[0,0,0
% 0.5,0,0
% 0.5,0.5,0
% 0,0.5,0
% 0.25,0,0.5
% 0.5,0.25,0.5
% 0.25,0.5,0.5
% 0,0.25,0.5
% 0,0,1
% 0.5,0,1
% 0.5,0.5,1
% 0,0.5,1
% 0.25,0,1.5
% 0.5,0.25,1.5
% 0.25,0.5,1.5
% 0,0.25,1.5
% 0,0,2
% 0.5,0,2
% 0.5,0.5,2
% 0,0.5,2];



%��ʼ�쳤��
delta_spring0=zeros(nelem_bar,1);
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





