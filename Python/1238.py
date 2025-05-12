while True:
    try:
        N = int(input())  
        
        for i in range(N):
            A, B = input().split()

            resultado=""
            for a, b in zip(A, B):
                resultado += a + b 
            resultado += A[len(B):] + B[len(A):]
            print(resultado)

    except EOFError:
        break
            
