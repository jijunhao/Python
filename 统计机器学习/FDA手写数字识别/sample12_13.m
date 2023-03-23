clear all
load digit.mat X T
[d,m,c]=size(T); c=3;

S=zeros(d,d);
for y=1:c
  mu(:,y)=mean(X(:,:,y),2);
  S=S+cov(X(:,:,y)')/c;
end
h=inv(S)*mu;
for y=1:c
  p(:,:,y)=h'*T(:,:,y)-repmat(sum(mu.*h)',[1,m])/2;
end
[pmax P]=max(p);
P=squeeze(P);
for y=1:c
  C(:,y)=sum(P==y);
end
C
