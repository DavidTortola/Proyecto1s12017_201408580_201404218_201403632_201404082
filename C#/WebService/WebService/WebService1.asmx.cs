﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace WebService
{
    /// <summary>
    /// Descripción breve de WebService1
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]

    // Para permitir que se llame a este servicio web desde un script, usando ASP.NET AJAX, quite la marca de comentario de la línea siguiente. 
    // [System.Web.Script.Services.ScriptService]
    public class WebService1: System.Web.Services.WebService
    {
        public static ArbolB arbolB = new ArbolB();
  

        [WebMethod]
        public string HelloWorld()
        {
            return "Hola a todos";
        }

        [WebMethod]
        public string Prueba(string par) {

            return par +  " Esto es en C#";

        }

        [WebMethod]
        public string insertar(string idrenta, string idactivo, string user, string empresa, string departamento, string fecha, string tiempo)
        {

            Rentas renta = new Rentas();
            renta.identificador = idrenta;
            renta.idActivo = idactivo;
            renta.usuario = user;
            renta.empresa = empresa;
            renta.departamento = departamento;
            renta.fecha = fecha;
            renta.tiempo = tiempo;

            arbolB.insertar(renta);
            arbolB.printGraphviz();

            return "Agregado";
        }

        [WebMethod]
        public string eliminar(string idActivo) {
            Rentas renta = new Rentas();

            renta.idActivo = idActivo;
            arbolB.Remover(renta);
            arbolB.printGraphviz();
            return "Transacciones eliminadas";

        }

    }
}
