
namespace Application
{

    class Foo
    {
        public Foo(){}
        public Foo(string name){name_= name;}
        public string GetName(){return name_;}
        private readonly string name_="";

    }
    class Bar
    {
        public Bar(){}
        public Bar(string name){name_= name;}
        public string GetName(){return name_;}
        private readonly string name_="";

    }


    class App
    {
        public App(){}   
        public static void Main()
        {
            Console.Write("Hello World\n");
            Foo foo = new("foo");
            Bar bar = new("bar");
            Console.WriteLine(foo.GetName() + bar.GetName());
        }
    }



}