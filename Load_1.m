function [f]=Load_1(load_step,f)    


cita = (0)*(load_step);

F=1;alpha_a=(cita/180)*pi;


f(4,1)=F*cos(alpha_a);
f(5,1)=F*sin(alpha_a);


end