
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

            Console.WriteLine(CustomCode.VersionCompare("2","2.0.0.0.1"));
            Console.WriteLine(CustomCode.VersionCompare("2","2.0.0.0"));
            Console.WriteLine(CustomCode.VersionCompare("2.0.1","1.2000.1"));

        }
    }

    public static class CustomCode
	{
		public static int VersionCompare( string version1, string version2 ) 
        {
            //Insert your code here
            int retcode=2, v1=0, v2 =0;
            string[] subsarr1 = version1.Split('.');
            string[] subsarr2 = version2.Split('.');
            List<string> subs1 = subsarr1.ToList();
            List<string> subs2 = subsarr2.ToList();

            foreach (string str in subs1){
                v1+= int.Parse(str);
            }

            foreach (string str in subs2){
                v2+= int.Parse(str);
            }

            if(v1 < v2){

                retcode = -1;
            }
            if(v1 > v2){
                retcode = 1;
            }
            else if(v1 == v2){ 
                foreach (string str in subs1){
                    if (subs2.Contains(str)){
                        if(subs1.IndexOf(str) < subs2.IndexOf(str)){
                            retcode = -1;
                        }
                        if(subs1.IndexOf(str) > subs2.IndexOf(str)){
                            retcode = 1;
                        }
                        else{
                            retcode =0;
                        }
                    }

                    if(retcode == -1 && int.Parse(subs1[0]) > int.Parse(subs2[0]))
                    {
                        retcode =1;
                    }
                }

            }

            return retcode;
		}
	}

}