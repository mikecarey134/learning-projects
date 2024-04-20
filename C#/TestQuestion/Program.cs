
using Application;





App app = new();
App.Main();

Console.WriteLine(CustomCode.VersionCompare("2","2.0.0.0.1"));
Console.WriteLine(CustomCode.VersionCompare("2","2.0.0.0"));
Console.WriteLine(CustomCode.VersionCompare("2.0.1","1.2000.1"));

