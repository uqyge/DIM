
%tic
clear
clc

break_step =  30;
format long e
fid10= fopen('Numerical Results.txt', 'w');
fid11= fopen('Convergence Results_1st step.txt', 'w');
fid12= fopen('Convergence Results_10th step.txt', 'w');

%==========================================================================
%================================= Input ==================================
%==========================================================================


Input_beam_cluster;

%==========================================================================
%============================ Initial displacment =========================
%==========================================================================

dis0=[1:mdof]'*0.01;

for ii=1:nrx
    nb1=3*lrx(ii)-2;
    dis0(nb1,1)=0;
end

for jj=1:nry
    nb2=3*lry(jj)-1;
    dis0(nb2,1)=0;
end

for rr=1:nrz
    nb3=3*lrz(rr);
    dis0(nb3,1)=0;
end

dis2=dis0;

%==========================================================================
%================================ weight ==================================
%==========================================================================

Num_load = 10;

[weight] = zhongli(lrz,nrz);

%==========================================================================
%=============================== Iteration ================================
%==========================================================================

num_sobol=0;

f_in = 'inputACT_abca';
sobol_ACT_T=csvread(strcat('python1\',f_in,'.csv'));

num_ACT_T=size(sobol_ACT_T,1);

ACT_sobol=sobol_ACT_T;

tic
scale_L=3;
scale_R=3;

forward = true;
if(forward)
    fid14 = fopen(strcat('python1\dis_23_forward_',f_in,'.csv'), 'w');
    fid15= fopen(strcat('python1\stress_cable_forward_',f_in,'.csv'), 'w');
    
    first = 1;
    step = 1;
    last = num_ACT_T;
else
    fid14 = fopen(strcat('python1\dis_23_backward_',f_in,'.csv'), 'w');
    fid15= fopen(strcat('python1\stress_cable_backward',f_in,'.csv'), 'w');
    
    first = num_ACT_T;
    step = -1;
    last = 1;
end

fprintf(fid15,'1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32\n');

fprintf(fid14,'n_step,ijk,num_load,A1,A2,A3,A4,Tup,Tmid,Tdown,23x,23y,23z\n');

for iii = first:step:last
    
    iii
    dis0=dis2;
    
    act_pct_1=ACT_sobol(iii,1);
    act_pct_2=ACT_sobol(iii,2);
    act_pct_3=ACT_sobol(iii,3);
    act_pct_4=ACT_sobol(iii,4);
    
    act_pct=[act_pct_1;act_pct_2;act_pct_3;act_pct_4];
    
    T_up=0;           %上绳温度
    T_mid=0;          %中绳温度
    T_down=0;           %下绳温度
    
    [epsilon_cable_temp0]...
        = T_cable(nelem_cable,T_mid,T_up,T_down);
    
    num_sobol=num_sobol+1;
    
    for load_step=1:Num_load
        
        load_step;
        
        incre = act_pct/Num_load;
        epsilon_cable_temp1=epsilon_cable_temp0/Num_load;
        
        da0 = [0.0255;0;0;0.0255];% No.1 and 4 clustered cables on the top surface;
        
        da = (load_step) * [incre(1);...
            incre(2);...
            incre(3);...
            incre(4)];
        epsilon_cable_temp=epsilon_cable_temp1*load_step;
        
        [fe]=Load_beam_cluster(load_step,nnode,mdof,lrx,lry,lrz,nrx,nry,nrz);
        
        %         [fe]=Load_grid2(nnode,load_step,mdof,lrx,lry,lrz,nrx,nry,nrz);
        
        f=fe;
        
        for n_step=1:break_step
            %             n_step
            
            %================================ Form Kt_spring ==============================================
            [Kt_spring,delta_spring,epsilon_spring,L0_spring,weight_spring]...
                = Assemble_Kt_spring(mdof,nod,nelem_spring,stiff_spring1,stiff_spring2,ele_spring,dis0,delta_spring0);
            
            
            %================================== Form Kt_bar ===============================================
            [Kt_bar,delta_bar,epsilon_bar,L0_bar,Ln_bar,weight_bar]...
                = Assemble_Kt_bar(mdof,nod,nelem_bar,e_bar,a_bar,ele_bar,dis0,delta_bar0);
            
            
            %============================== Form Kt_cable ==================================================
            [Kt_cable,delta_cable,epsilon_cable,L0_cable,Ln_cable,weight_cable]...
                = Assemble_Kt_cable(mdof,nod,nelem_cable,e_cable,a_cable,ele_cable,dis0,delta_cable0,epsilon_cable_temp);
            
            
            %============================= Form Kt_clusters ================================================
            [Kt_cluster,delta_cluster,epsilon_cluster,L0_cluster,Ln_cluster,weight_cluster]...
                = Assemble_Kt_cluster(mdof,cluster,m,n,nod,e_cluster,a_cluster,ele_cluster,dis0,delta_cluster0,da0,da);
            
            weight = -(weight_spring + weight_bar + weight_cable + weight_cluster);
            
            
            %========================== Boundary condition for Kt ==========================================
            [Kt] = Assemble_Kt(Kt_spring,Kt_bar,Kt_cable,Kt_cluster,lrx,lry,lrz,nrx,nry,nrz);
            
            
            %============================ Internal nodal forces ============================================
            [q,q_bar,q_cable,q_cluster,NF_spring,NF_bar,NF_cable,NF_cluster] = Internal_force(mdof,cluster,m,n,nod,nelem_spring,nelem_bar,nelem_cable,e_bar,e_cable,e_cluster,...
                a_bar,a_cable,a_cluster,ele_spring,ele_bar,ele_cable,ele_cluster,dis0,L0_bar,L0_cable,L0_cluster,L0_spring,stiff_spring1,stiff_spring2,epsilon_cable_temp);
            
            
            %==================== Boundary condition for out-of-balance forces =============================
            [df,f] = Get_df(f,q,weight,lrx,lry,lrz,nrx,nry,nrz);
            
            
            %============================== Solve "Kt*dU=dF" ===============================================
            delta_dis = Kt\df;
            
            
            %================================= "U1=U0+dU" ==================================================
            dis1 = dis0 + delta_dis;
            
            dis0 = dis1;
            %============================= Convergece criteria =============================================
            
            err_f = norm(df);
            
            if(err_f<1e-5)
                'Yes!!!';
                break
            end
            
            if(load_step==1)
                fprintf(fid11, '%6i %20.6e\n', n_step, err_f);
            end
            
            if(load_step==10)
                fprintf(fid12, '%6i %20.6e\n', n_step, err_f);
            end
            
            %=================================== "U0=U1" ===================================================
            
        end
        
        fprintf(fid10, '%6i %6i\n', load_step, n_step);
        
        
        %%%%%%%%%%%%%%%%%% each load_step picture
        %     dis1(:,1)=dis1(:,1)*1;
        %     figure(2);
        %
        %     [nod_now]=Disposal_grid2(nnode,nod,m,n,nelem_spring,nelem_bar,...
        %         nelem_cable,cluster,ele_spring,ele_bar,ele_cable,ele_cluster,dis1);
        
    end
    
    [nod_now]=nod_now_result(nnode,nod,m,n,nelem_spring,nelem_bar,...
        nelem_cable,cluster,ele_spring,ele_bar,ele_cable,ele_cluster,dis1);
    
    nod_000 = [26.5000000000000,39.7500000000000,0;79.3220677260045,12.3351489396036,0.0992035026548445;0,-13.2500000000000,0;53.0087147639479,-40.6300144322402,-0.865453081740054;...
        52.3313501941159,38.1085214377346,30.5567297980734;0,13.2500000000000,30;79.3379615489612,-14.4899984960731,29.8438701279774;27.2078850703319,-39.6304465317048,29.7454334994341;...
        91.8152214376121,37.7314789080797,-0.926648423125315;144.632414277766,7.41915001481255,-0.121508553780224;65.9914961793518,-14.3565502691039,0.0765000814888062;118.723310210205,-44.7904521579717,-0.991158422629326;...
        117.726468909301,34.3404903180150,29.4192745591611;65.6087403832400,12.0002766180268,30.2266166195369;145.196309745074,-19.0611219657251,29.9272272909059;92.9534143815626,-41.3919867230393,29.4747904775614;...
        157.535540550642,33.6576579633543,-1.11739715229474;210.831241539454,6.35968534141468,0.0435781058352010;131.358740320793,-19.3005932072914,-0.163807701517905;184.142148981115,-46.7683054613913,-0.237374037462820;...
        183.253138924127,32.6004124733525,29.5609111019889;131.412754746299,7.40286035090904,29.6805028620628;210.574083403007,-20.2067325245193,30.0184329416879;158.332414276323,-45.0587507979157,30.3345269782941];
    
    dis_now = nod_now - nod_000;
    
    dis_23x=dis_now(23,1);
    dis_23y=dis_now(23,2);
    dis_23z=dis_now(23,3);
    
    stress_cable=(NF_cable/a_cable);
    
    if n_step==break_step
        
        ijk=2;
        
        fprintf(fid14, '%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i\n',n_step, ijk,num_sobol,act_pct_1, act_pct_2,act_pct_3, act_pct_4,T_up,T_mid,T_down,dis_23x,dis_23y,dis_23z);
        fprintf(fid15,'%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i\n',stress_cable);
        
        continue
        
    else
        if abs(dis1(23*3-2,1))>150
            ijk=0;
            
        else
            ijk=1;
            
%             [nod_now]=Disposal_grid2(nnode,nod,m,n,nelem_spring,nelem_bar,...
%                 nelem_cable,cluster,ele_spring,ele_bar,ele_cable,ele_cluster,dis1);
            
        end
        
    end
    
    fprintf(fid14, '%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i\n',n_step, ijk,num_sobol,act_pct_1, act_pct_2,act_pct_3, act_pct_4,T_up,T_mid,T_down,dis_23x,dis_23y,dis_23z);
    
    fprintf(fid15,'%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i,%6i\n',stress_cable);
    
    continue
    
end
% Focus on the displacement at Node 23

%==========================================================================
%==========================================================================
%==========================================================================
fclose(fid10);
fclose(fid14);
fclose(fid15);
toc

dis1(3*23)
dis1(3*23-1)






