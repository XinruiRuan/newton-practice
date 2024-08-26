def optimize(start, fun, tol=1e-6, max_iter=1000, h=1e-5):
    # x = start
    
    for i in range(max_iter):
        # Calculate first derivative using finite difference
        f_prime = (fun(x + h) - fun(x - h)) / (2 * h)
        
        # Calculate second derivative using finite difference
        f_double_prime = (fun(x + h) - 2 * fun(x) + fun(x - h)) / (h ** 2)
        
        if f_double_prime == 0:  # Avoid division by zero
            print("Second derivative is zero. Stopping optimization.")
            break
        
        # Newton's update step
        x_new = x - f_prime / f_double_prime
        
        # Check stopping criterion
        if abs(x_new - x) < tol:
            print(f"Converged in {i+1} iterations.")
            return x_new
        
        x = x_new
    
    print("Maximum iterations reached without convergence.")
    return x