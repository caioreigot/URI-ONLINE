using System; 

class ID1075 {

    static void Main(string[] args) { 

            int n = Int32.Parse(Console.ReadLine());

            for (int i = 0; i <= 10000; i++)
            {
                if (i % n == 2)
                    Console.WriteLine(i);
            }

    }

}