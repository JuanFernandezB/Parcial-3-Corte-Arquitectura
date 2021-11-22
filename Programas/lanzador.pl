#!/usr/bin/perl

#Fichero especializado para la ejecución en los ejecutables
$path= "/home/juan/Escritorio/Arquitectura/ParcialTercerCorte";

@Ejecutables=("MMcpp","MM1c");

@VectorSize=("200","500","1000","1500","2000");

$repeticiones=30;

foreach $exe(@Ejecutables){
    foreach $ves(@VectorSize)
    {
        $file = "$path/"."$exe"."-Size-"."$ves".".txt";
        #print "$file\n"; #Este es el nombre del archivo vale
        for($i=0;$i<$repeticiones;$i++)
        {
            system("$path/$exe $ves >> $file");
            #print "$path/$exe $ves \n";
        }
    }
}
