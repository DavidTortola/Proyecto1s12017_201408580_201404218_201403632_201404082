using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebService
{
    public class NodoArbolB
    {
        public static int m = 5;
        private static int numPunteros = m + 1;
        private static int numLlaves = m;
        public Boolean hoja = true;
        public int ULlave = 1;
        public Rentas[] llaves = new Rentas[numLlaves];
        public NodoArbolB[] punteros = new NodoArbolB[numPunteros];
        public NodoArbolB Padre;
        public NodoArbolB(Object objeto)
        {
            Rentas renta = (Rentas) objeto;


            llaves[0] = renta;

        }

        public NodoArbolB()
        {
            for (int i = 0; i < m - 1; i++)
            {
                llaves[i] = null;
            }
            this.Padre = null;
        }
    }
}