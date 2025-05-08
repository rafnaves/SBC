using System;

public class Programa
{
    public static void Main(){
        {
            while (true) //Loop em C# enquato não receber break
            {
                string[] entrada = Console.ReadLine().Split(); //lendo a linha de entrada e armazenando na lista
                int H1 = int.Parse(entrada[0]); //# i[0]
                int M1 = int.Parse(entrada[1]);
                int H2 = int.Parse(entrada[2]);
                int M2 = int.Parse(entrada[3]); // i[3]
                
                // quando receber 0 0 0 0, parar o programa
                if (H1 == 0 && M1 == 0 && H2 == 0 && M2 == 0)
                break;
                
                // calculo, transformando horas e minutos, somando com os minutos
                int inicio = H1 * 60 + M1;
                int fim = H2 * 60 + M2;
                
                
                int minutos = fim - inicio;
                // Se a diferença deu negativa, quer dizer que o alarme é no dia seguinte, então somamos 1440 (minutos de 1 dia) pra corrigir.
                if (minutos < 0)
                    minutos += 1440;
                Console.WriteLine(minutos);
                
                
        }
    }
}
}