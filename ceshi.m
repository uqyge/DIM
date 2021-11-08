fid20= fopen('displace_23.csv','w');
fprintf(fid20,'A1,A2,A3,A4,Tup,Tmid,Tdown,23x,23y,23z\n');
date=csvread('gauss1_samples.csv',1,0);
a=[1,2,3];
result(1,1:7)=date(1,1:7);
result(1,8:10)=a(1,1:3);