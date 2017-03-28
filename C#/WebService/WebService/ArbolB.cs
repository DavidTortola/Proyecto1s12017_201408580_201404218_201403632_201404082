using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace WebService
{
    public class ArbolB
    {
        List<Rentas> lstnodos = new List<Rentas>();
        List<Rentas> lstactivos = new List<Rentas>();

        public NodoArbolB raiz;
        public ArbolB()
        {
            this.raiz = null;
        }

        //METODO DE BUSQUEDA , PERMITIRA BUSCAR ELEMENTOS EN EL ARBOL 
        //ALGORITMO REURSIVO ESENCIAL PARA LA INSERCION , ELIMINACION


        //METODO DE BUSQUEDA , PERMITIRA BUSCAR ELEMENTOS EN EL ARBOL 
        //ALGORITMO REURSIVO ESENCIAL PARA LA INSERCION , ELIMINACION
        private NodoArbolB buscar(Rentas renta, NodoArbolB node)
        {
            if (node != null)
            {
                int i = 1;
                while (i <= node.ULlave && (string.Compare(node.llaves[i - 1].identificador, renta.identificador) < 0))

                    i++;
                if (i > node.ULlave || (string.Compare(node.llaves[i - 1].identificador, renta.identificador) > 0))
                    return buscar(renta, node.punteros[i - 1]);
                else
                    return node;
            }
            else
            {
                return null;
            }
        }

        //OBTENER VALOR DE ATRIBUTO KEY (MOSTRAR)
        //public int get(int llave)
        //{
        //    int k = 0;
        //    if (this.existe(llave))
        //    {
        //        NodoArbolB nodo = this.buscar(llave, this.raiz);
        //        for (int i = 0; i < 4; i++)
        //        {
        //            if (nodo.llaves[i] == llave)
        //            {
        //                k = nodo.llaves[i];
        //                break;
        //            }
        //        }
        //    }
        //    return k;
        //}

        //OBETNER VALOR DE ATRIBUTO KEY REMPLZAR CON ATRIBUTO N (MODIFICAR)
        public void set(Rentas renta, Rentas Reemplazo)
        {
            if (this.existe(renta))
            {
                NodoArbolB nodo = this.buscar(renta, this.raiz);
                this.ReemplazarLlave(nodo, renta, Reemplazo);
            }
        }

        //METODO QUE VRIFICAR QUE EXISTA UN ATRIBUTO KEY 
        public Boolean existe(Rentas renta)
        {
            if (buscar(renta, this.raiz) != null)
                return true;
            else
                return false;
        }
        //ALGORITMO DE INSERCION 
        public void insertar(Rentas renta)
        {
            if (this.raiz == null)
            {
                this.raiz = new NodoArbolB(renta);
                return;
            }
            NodoArbolB nodo = raiz;

            while (nodo.hoja == false)
            {
                int i = 1;
                while (i <= nodo.ULlave && (nodo.llaves[i - 1].identificador.CompareTo(renta.identificador)) != 1)
                    i++;
                nodo = nodo.punteros[i - 1];
            }

            Boolean posInLeaf = true;
            NodoArbolB node1 = null;
            NodoArbolB node2 = null;

            while (true)
            {
                int i = 1;
                while (i <= nodo.ULlave && (nodo.llaves[i - 1].identificador.CompareTo(renta.identificador)) != 1)
                    i++;

                if (i <= nodo.ULlave)
                {
                    int finalPointer = nodo.ULlave - 1;
                    while (finalPointer >= i - 1)
                    {
                        nodo.llaves[finalPointer + 1] = nodo.llaves[finalPointer];

                        nodo.punteros[finalPointer + 2] = nodo.punteros[finalPointer + 1];
                        finalPointer--;
                    }
                }

                nodo.llaves[i - 1] = renta;

                nodo.ULlave = nodo.ULlave + 1;

                if (node1 != null && node2 != null)
                {
                    nodo.punteros[i - 1] = node1;
                    nodo.punteros[i] = node2;

                    node1 = null;
                    node2 = null;
                }

                int order = 6;
                //Máximo de claves permitidas en un Árbol B = m-1
                if (nodo.ULlave < order - 1)
                {
                    return;
                }
                else
                {
                    int posInMiddleKey = (order / 2) - 1;

                    renta = nodo.llaves[posInMiddleKey];


                    node1 = nodo;
                    node2 = new NodoArbolB();

                    if (posInLeaf)
                    {
                        node1.hoja = true;
                        node2.hoja = true;
                    }
                    else
                    {
                        node1.hoja = false;
                        node2.hoja = false;
                    }

                    node1.llaves[posInMiddleKey] = null;

                    node1.ULlave = (order / 2) - 1;
                    node2.ULlave = (order / 2) - 1;
                    int posInNode1 = posInMiddleKey + 1;
                    int posInNode2 = 0;
                    while (posInNode1 < order - 1)
                    {

                        node2.llaves[posInNode2] = node1.llaves[posInNode1];

                        node1.llaves[posInNode1] = null;


                        node2.punteros[posInNode2] = node1.punteros[posInNode1];
                        if (node2.punteros[posInNode2] != null)
                        {
                            node2.punteros[posInNode2].Padre = node2;
                        }

                        node1.punteros[posInNode1] = null;

                        //----------------------------------------------

                        posInNode1++;
                        posInNode2++;

                        if (posInNode1 == order - 1)
                        {
                            node2.punteros[posInNode2] = node1.punteros[posInNode1];
                            if (node2.punteros[posInNode2] != null)
                            {
                                node2.punteros[posInNode2].Padre = node2;
                            }

                            node1.punteros[posInNode1] = null;
                        }

                    }

                    if (nodo == this.raiz)
                    {

                        NodoArbolB auxRaiz = new NodoArbolB(renta);
                        auxRaiz.hoja = false;
                        auxRaiz.punteros[0] = node1;
                        auxRaiz.punteros[1] = node2;

                        node1.Padre = auxRaiz;
                        node2.Padre = auxRaiz;

                        this.raiz = auxRaiz;
                        return;

                    }
                    else
                    {
                        nodo = nodo.Padre;
                        node2.Padre = node1.Padre;
                        posInLeaf = false;
                    }

                }
            }
        }

        //NODOS CON PRECEDENCIA 
        public NodoArbolB PrecedenciaNodo(Rentas renta, NodoArbolB nodo)
        {
            int i = 1;
            while (i <= nodo.ULlave)
            {
                if (nodo.llaves[i - 1].identificador.Equals(renta.identificador))
                {
                    nodo = nodo.punteros[i];
                    break;
                }
                i++;
            }
            while (true)
            {
                if (nodo.hoja)
                {
                    return nodo;
                }
                else
                {
                    nodo = nodo.punteros[0];
                }
            }
        }

        //ALGORITMO PARA REEMPLAZAR 
        public void ReemplazarLlave(NodoArbolB nodo, Rentas renta, Rentas renta2)
        {
            int i = 1;
            while (i <= nodo.ULlave)
            {
                if (nodo.llaves[i - 1].identificador.Equals(renta.identificador))
                {
                    nodo.llaves[i - 1] = renta2;
                    break;
                }
                i++;
            }
        }

        //ALGORITMO QUE ELMININA KEYS EN NODOS HOJA
        public void EliminarHoja(NodoArbolB nodo, Rentas renta)
        {
            int i = 0;
            while (i < nodo.ULlave)
            {
                if (nodo.llaves[i].identificador.Equals(renta.identificador))
                {
                    while (i < nodo.ULlave - 1)
                    {
                        nodo.llaves[i] = nodo.llaves[i + 1];

                        i++;
                    }
                    nodo.llaves[nodo.ULlave - 1] = null;

                    nodo.ULlave--;
                }
                else
                {
                    i++;
                }
            }
        }

        //VERIFICA EL MINIMO
        private Boolean VerificarMinimo(NodoArbolB nodo)
        {
            if (nodo == this.raiz)
            {
                if (nodo.ULlave == 0)
                {
                    this.raiz = null;
                }
                return true;
            }
            int minKeys = 2;
            if (nodo.ULlave >= minKeys)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        //LADO IZQUIRDO DEL ARBOL UTILIZADO PARA COMPARACION ENTRE NODOS 
        private NodoArbolB izquierda(NodoArbolB nodo)
        {
            int i = 0;
            NodoArbolB Padre = nodo.Padre;
            while (i <= Padre.ULlave)
            {
                if (Padre.punteros[i] == nodo)
                {
                    if (i == 0)
                        return null;
                    else
                        return Padre.punteros[i - 1];
                }
                i++;
            }
            return null;
        }

        //LADO DERECHO DEL ARBOL UTILIZADO PARA COMPARACION COMPARACION ENTRE NODOS
        private NodoArbolB derecha(NodoArbolB nodo)
        {
            int i = 0;
            NodoArbolB Padre = nodo.Padre;
            while (i <= Padre.ULlave)
            {
                if (Padre.punteros[i] == nodo)
                {
                    if (i == Padre.ULlave)
                        return null;
                    else
                        return Padre.punteros[i + 1];
                }
                i++;
            }
            return null;
        }

        private void TomardeDerecha(NodoArbolB nodo)
        {
            NodoArbolB Padre = nodo.Padre;
            int i = 0;
            while (i < Padre.ULlave)
            {
                if (Padre.punteros[i] == nodo)
                {
                    NodoArbolB derecha = Padre.punteros[i + 1];
                    nodo.llaves[nodo.ULlave] = Padre.llaves[i];

                    nodo.ULlave++;
                    nodo.punteros[nodo.ULlave] = derecha.punteros[0];
                    Padre.llaves[i] = derecha.llaves[0];

                    int k = 0;
                    while (k < derecha.ULlave - 1)
                    {
                        derecha.llaves[k] = derecha.llaves[k + 1];

                        derecha.punteros[k] = derecha.punteros[k + 1];
                        k++;
                    }
                    derecha.llaves[k] = null;

                    derecha.punteros[k] = derecha.punteros[k + 1];
                    derecha.ULlave--;
                }
                i++;
            }
        }

        private void TomardeIzquierda(NodoArbolB nodo)
        {
            NodoArbolB Padre = nodo.Padre;
            int i = 0;
            while (i <= Padre.ULlave)
            {
                if (Padre.punteros[i] == nodo)
                {
                    NodoArbolB izquierda = Padre.punteros[i - 1];
                    int k = 0;
                    while (k < nodo.ULlave)
                    {
                        nodo.llaves[k + 1] = nodo.llaves[k];

                        nodo.punteros[k + 1] = nodo.punteros[k];
                        k++;
                    }
                    nodo.punteros[k + 1] = nodo.punteros[k];
                    nodo.llaves[0] = Padre.llaves[i - 1];

                    nodo.punteros[0] = izquierda.punteros[izquierda.ULlave];
                    Padre.llaves[i - 1] = izquierda.llaves[izquierda.ULlave - 1];

                    izquierda.llaves[izquierda.ULlave - 1] = null;

                    izquierda.punteros[izquierda.ULlave] = null;
                    izquierda.ULlave--;
                    nodo.ULlave++;
                    break;
                }
                i++;
            }
        }

        //METODO QUE CREA UNA NUEVA RAIZ
        //EN LA ELIMINACION EXISTE LA POSIBILIDAD QUE SE ELIMINE UNA RAIZ 
        //METODO PERMITE CREAR UNA NUEVA RAIZ PARA QUE EL ARBOL NO SE ALTERE
        private void NuevaRaiz(NodoArbolB left, NodoArbolB right)
        {
            left.llaves[left.ULlave] = raiz.llaves[0];

            left.ULlave++;
            int leftPointer = left.ULlave;
            int i = 0;
            while (i < right.ULlave)
            {
                left.llaves[leftPointer] = right.llaves[i];

                if (right.punteros[i] != null)
                {
                    left.punteros[leftPointer] = right.punteros[i];
                    right.punteros[i].Padre = left;
                }
                i++; leftPointer++; left.ULlave++;
            }
            if (right.punteros[i] != null)
            {
                left.punteros[leftPointer] = right.punteros[i];
                right.punteros[i].Padre = left;
            }
            raiz = left;
            raiz.Padre = null;
        }

        //METODO COMBINAR , PERMITE COMBINAR LOS DATOS EN EL MOMENTO DE LA ELIMINACION
        //INDISPENSABLE PARA LA REDUCCION DE PAGINAS O EL INCREMENTO DE DATOS EN LAS PAGINAS
        private void combinar(NodoArbolB nodo)
        {
            if (derecha(nodo) != null)
            {
                NodoArbolB Padre = nodo.Padre;
                int i = 0;
                while (i < Padre.ULlave)
                {
                    if (Padre.punteros[i] == nodo)
                    {
                        nodo.llaves[nodo.ULlave] = Padre.llaves[i];
                        nodo.ULlave++;
                        NodoArbolB partner = derecha(nodo);
                        int k = 0;
                        while (k < partner.ULlave)
                        {
                            nodo.llaves[nodo.ULlave] = partner.llaves[k];
                            nodo.punteros[nodo.ULlave] = partner.punteros[k];
                            nodo.ULlave++;
                            k++;
                        }
                        nodo.punteros[nodo.ULlave] = partner.punteros[k];
                        int pointer = i;
                        while (pointer < Padre.ULlave)
                        {
                            Padre.llaves[pointer] = Padre.llaves[pointer + 1];
                            Padre.punteros[pointer + 1] = Padre.punteros[pointer + 2];
                            pointer++;
                        }
                        Padre.ULlave--;
                        break;
                    }
                    i++;
                }
            }
            else
            {
                combinar(izquierda(nodo));
            }
        }
        public void Lista(Rentas renta, NodoArbolB nodo)
        {

            if (nodo.punteros != null)
            {
                for (int i = 0; i < nodo.punteros.Length - 1; i++)
                {
                    if (nodo.punteros[i] != null)
                        Lista(renta, nodo.punteros[i]);
                }
            }

            for (int j = 0; j < nodo.llaves.Length - 1; j++)
            {
                if (nodo.llaves[j] != null)
                {
                    if (nodo.llaves[j].idActivo.Equals(renta.idActivo))
                    {
                        Console.WriteLine("Raiz: " + nodo.llaves[j].identificador + " Activo:" + nodo.llaves[j].idActivo);
                        lstnodos.Add(nodo.llaves[j]);

                    }
                }


            }
        }


        public void ListaActivo(Rentas renta, NodoArbolB nodo)
        {

            if (nodo.punteros != null)
            {
                for (int i = 0; i < nodo.punteros.Length - 1; i++)
                {
                    if (nodo.punteros[i] != null)
                        ListaActivo(renta, nodo.punteros[i]);
                }
            }

            for (int j = 0; j < nodo.llaves.Length - 1; j++)
            {
                if (nodo.llaves[j] != null)
                {
                    if (nodo.llaves[j].usuario.Equals(renta.usuario) && nodo.llaves[j].empresa.Equals(renta.empresa) && nodo.llaves[j].departamento.Equals(renta.departamento) && nodo.llaves[j].rentado == true)
                    {
                        lstactivos.Add(nodo.llaves[j]);

                    }
                }


            }
        }

        //    for (int i = 0; i < nodo.punteros.Length - 1; i++)
        //    {
        //        if (nodo.punteros[i] != null)
        //        {
        //            for (int h = 0; h < nodo.punteros[i].punteros.Length - 1; h++)
        //            {
        //                if (nodo.punteros[i].punteros[h] != null)
        //                {
        //                    Lista(renta, nodo.punteros[i]);
        //                }
        //                else
        //                {
        //                    for (int j = 0; j < nodo.llaves.Length - 1; j++)
        //                    {
        //                        if (nodo.punteros[i].llaves[j] != null)
        //                        {
        //                            if (nodo.punteros[i].llaves[j].idActivo.Equals(renta.idActivo))
        //                            {
        //                                Console.WriteLine("Raiz: " + nodo.punteros[i].llaves[j].identificador + " Activo:" + nodo.punteros[i].llaves[j].idActivo);
        //                                lstnodos.Add(nodo.punteros[i].llaves[j]);

        //                            }
        //                        }
        //                    }
        //                }
        //            }
        //        }
        //    }
        //}



        //for (int i = 0; i < nodo.punteros.Length - 1; i++)
        //{
        //    if (nodo.punteros[i] != null)
        //    {
        //        if (nodo.punteros[i].punteros != null)
        //        {
        //            Lista(renta, nodo.punteros[i]);
        //        }
        //        for (int j = 0; j < nodo.llaves.Length - 1; j++)
        //        {
        //            if (nodo.punteros[i].llaves[j] != null)
        //            {
        //                if (nodo.punteros[i].llaves[j].idActivo.Equals(renta.idActivo))
        //                {
        //                    Console.WriteLine("Raiz: " + nodo.punteros[i].llaves[j].identificador + " Activo:" + nodo.punteros[i].llaves[j].idActivo);
        //                    lstnodos.Add(nodo.punteros[i].llaves[j]);

        //                }

        //            }
        //        }
        //    }
        //}



        //METODO ELIMINAR , ELIMINA ID EN EL ARBOL SEGUN PARAMETRO ENVIADO
        public void Remover(Rentas renta)
        {
            //BUSCA LA CLAVE

            Lista(renta, this.raiz);

            for (int i = 0; i < lstnodos.Count; i++)
            {


                NodoArbolB nodo = buscar(lstnodos[i], this.raiz);

                if (nodo != null)
                {
                    //ELIMINACION SI Y SOLO SI EL NODO NO ES HOJA 
                    if (nodo.hoja == false)
                    {
                        NodoArbolB hoja = PrecedenciaNodo(lstnodos[i], nodo);
                        Rentas presedencia = hoja.llaves[0];
                        ReemplazarLlave(nodo, lstnodos[i], presedencia);
                        nodo = hoja;
                        EliminarHoja(hoja, presedencia);
                    }
                    else
                    {
                        //ELIMINACION NODO EN HOJA 
                        EliminarHoja(nodo, lstnodos[i]);
                    }

                    //ALGORITMO QUE SE MANTIENE EJECUTANDO DURANTE LA ELIMINACION 
                    //INSTRUCCIONES QUE CREAN NUEVAS RAICES, COMBINAN , MUEVEN IZQ DER EN CASO QUE SE ELIMINO
                    //NODOS EN LOS CUALES SE REQUIERE RESTRUCTURAR EL ARBOL ARMANDO NUEVAS PAGINAS
                    while (true)
                    {
                        if (VerificarMinimo(nodo))
                        {
                            break;
                        }
                        else if (derecha(nodo) != null && derecha(nodo).ULlave > 2)
                        {
                            TomardeDerecha(nodo);
                            break;
                        }
                        else if (izquierda(nodo) != null && izquierda(nodo).ULlave > 2)
                        {
                            TomardeIzquierda(nodo);
                            break;
                        }
                        else if (nodo.Padre == this.raiz)
                        {
                            if (nodo.Padre.ULlave == 1)
                            {
                                if (derecha(nodo) != null)
                                {
                                    NuevaRaiz(nodo, derecha(nodo));
                                }
                                else if (izquierda(nodo) != null)
                                {
                                    NuevaRaiz(izquierda(nodo), nodo);
                                }
                            }
                            else
                            {
                                combinar(nodo);
                            }
                            break;
                        }
                        else
                        {
                            combinar(nodo);
                            nodo = nodo.Padre;

                        }
                    }
                }
            }
        }
        public void printGraphviz()
        {
            NodoArbolB auxNode = this.raiz;

            StreamWriter sw = new StreamWriter("C:\\Reportes\\ArbolB.txt");
            sw.WriteLine("digraph G {");
            sw.WriteLine("\t rankdir = TB; \n");
            sw.WriteLine("\t node[shape=record]; \n");
            sw.WriteLine("\t subgraph clusterBTree { \n");
            sw.WriteLine("\t label = \"HISTORIAL DE TRANSACCIONES\"; \n");
            sw.WriteLine("\t node [shape=record];\nnode [style=filled];\nnode [fillcolor=\"#EEEEEE\"];\nnode [color=\"#8C8C8E\"];\nedge [color=\"#31CEF0\"]; \n");
            print(auxNode, sw);
            sw.WriteLine("\t } \n");
            sw.WriteLine("\t } \n");
            sw.Close();
            String dotPath = "dot.exe";
            String fileInputPath = "C:\\Reportes\\ArbolB.txt";
            String fileOutputPath = "C:\\Reportes\\ArbolB.png";
            String tParam = "-Tpng";
            String tOParam = "-o";
            String[] cmd = new String[5];
            cmd[0] = dotPath;
            cmd[1] = tParam;
            cmd[2] = fileInputPath;
            cmd[3] = tOParam;
            cmd[4] = fileOutputPath;

            ExecuteCommand(cmd[0] + " " + cmd[1] + " " + cmd[2] + " " + cmd[3] + " " + cmd[4]);
        }

        //METODO PARA ABRIR CONSOLA Y EJECUTAR COMANDOS PARA GRAPVIZ
        static void ExecuteCommand(string _Command)
        {
            //Indicamos que deseamos inicializar el proceso cmd.exe junto a un comando de arranque. 
            //(/C, le indicamos al proceso cmd que deseamos que cuando termine la tarea asignada se cierre el proceso).
            //Para mas informacion consulte la ayuda de la consola con cmd.exe /? 
            System.Diagnostics.ProcessStartInfo procStartInfo = new System.Diagnostics.ProcessStartInfo("cmd", "/c " + _Command);
            // Indicamos que la salida del proceso se redireccione en un Stream
            procStartInfo.RedirectStandardOutput = true;
            procStartInfo.UseShellExecute = false;
            //Indica que el proceso no despliegue una pantalla negra (El proceso se ejecuta en background)
            procStartInfo.CreateNoWindow = false;
            //Inicializa el proceso
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.StartInfo = procStartInfo;
            proc.Start();
            //Consigue la salida de la Consola(Stream) y devuelve una cadena de texto
            string result = proc.StandardOutput.ReadToEnd();
            //Muestra en pantalla la salida del Comando
            Console.WriteLine(result);
        }

        //ALGORITMO RECURSIVO , RECORRE EL ARBOL Y ESCRIBE EN EL TXT PARA PODER GRAFICAR
        private void print(NodoArbolB nodo, StreamWriter sw)
        {
            if (nodo != null)
            {
                if (nodo.Padre != null)
                {
                    sw.WriteLine("\"" + nodo.Padre.llaves[0].identificador + "\" -> \"" + nodo.llaves[0].identificador + "\"");
                }
                sw.WriteLine("\n\"" + nodo.llaves[0].identificador + "\"[label=\" ID Transaccion: ");
                for (int i = 0; i < 4; i++)
                {
                    if (i != 0)
                    {
                        sw.WriteLine(" | ID Transaccion: ");
                    }
                    if (nodo.llaves[i] != null)
                    {
                        sw.WriteLine(nodo.llaves[i].identificador);

                    }
                    else { sw.WriteLine(0); }


                }
                sw.WriteLine("\"];\n");
                for (int i = 0; i < 5; i++)
                {
                    if (nodo.punteros[i] != null)
                        print(nodo.punteros[i], sw);
                }
            }
        }
        public void setRenta(Rentas re){
            setRenta(re, raiz);
        }
        public void setRenta(Rentas renta, NodoArbolB nodo)
        {

            if (nodo.punteros != null)
            {
                for (int i = 0; i < nodo.punteros.Length - 1; i++)
                {
                    if (nodo.punteros[i] != null)
                        setRenta(renta, nodo.punteros[i]);
                }
            }

            for (int j = 0; j < nodo.llaves.Length - 1; j++)
            {
                if (nodo.llaves[j] != null)
                {
                    if (nodo.llaves[j].idActivo.Equals(renta.idActivo) && nodo.llaves[j].rentado == true)
                    {
                        nodo.llaves[j].rentado = false;

                    }
                }


            }
        }

        public List<string> ActivosActivos(string usuario, string empresa, string departamento)
        {
            Rentas rent = new Rentas();
            rent.usuario = usuario;
            rent.empresa = empresa;
            rent.departamento = departamento;

            ListaActivo(rent, raiz);


            List<string> auxlista = new List<string>();
            for (int i = 0; i < lstactivos.Count; i++)
            {
                Rentas aux = lstactivos[i];
                auxlista.Add(aux.idActivo + "," + aux.nombre + "," + aux.descripcion);

            }



            return auxlista;
        }
    }
}