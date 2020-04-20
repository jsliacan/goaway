N = 5000;  % number of nodes
p = 0.0016 % prob of 1

A = sparse(N, N); % adjacency matrix <----- ! NOT a matrix !

% link density of 0.0016
for i = 1:N
    for j = 1:N
        x = rand;
        if x < p
            % set adj(i,j) = 1
            A(i,j) = 1;
        else 
            % set adj(i,j) = 0
            A(i,j) = 0;
        end
    end
end

% FASTER 
A = sprand(N, N, p);
A = (A ~= 0)            % set every entry of A to 1 (True) if non-zero and leave it 0 otherwise.
