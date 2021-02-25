using System; 

class ID1074 {

    static void Main(string[] args) { 
        
        int N = Int32.Parse(Console.ReadLine());
        string[] results = new string[N];
        
        for (int i = 0; i < N; i++)
        {
            int value = Int32.Parse(Console.ReadLine());

            if (value == 0)
                results[i] = "NULL";

            else if (value % 2 == 0)
            {
                if (value > 0)
                    results[i] = "EVEN POSITIVE";
                else
                    results[i] = "EVEN NEGATIVE";
            }
            else if (value % 2 != 0)
            {
                if (value > 0)
                    results[i] = "ODD POSITIVE";
                else
                    results[i] = "ODD NEGATIVE";
            }
        }

        foreach (string resultado in results)
            Console.WriteLine(resultado);

    }

}