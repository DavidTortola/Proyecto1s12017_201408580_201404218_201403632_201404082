/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Logica;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;

/**
 *
 * @author Andree
 */
public class Flask {

    public static OkHttpClient webClient = new OkHttpClient();

    public Flask() {

    }

    public boolean Login(String user, String pass, String empresa, String departamento) {
        //Metodo para buscar en la matriz
        boolean estado;
        String arreglo = user + "$" + pass + "$" + empresa + "$" + departamento;
        String cadena = sendText(arreglo, "login");
        if (cadena.equals("false")) {
            return false;
        } else {
            String[] devolucion = cadena.split(",");
            if (devolucion[1].equals(user) && devolucion[2].equals(pass)) {
                return true;
            } else {
                return false;
            }
        }
    }

    public String Registrar(String user, String pass, String nombre, String empresa, String departamento) {
        String arreglo = user + "$" + pass + "$" + nombre + "$" + empresa + "$" + departamento;
        return sendText(arreglo, "registrar");

    }

    public String[] obtenerIdArbol(String user, String empresa, String departamento) {
        
        String[] valores = sendText(user, empresa, departamento, "obtenerdatos").split(",");

        return valores;
    }

    public String EliminarActivo(String user, String empresa, String departamento, String id) {

        sendText(user, empresa, departamento, id, "eliminaractivo");
        
        new WebService1().getWebService1Soap().eliminar(id);

        return "Eliminado";
    }

    public String RegistrarActivo(String usuario, String producto, String Descripcion, String empresa, String departamento) {
        String arreglo = usuario + "$" + producto + "$" + Descripcion + "$" + empresa + "$" + departamento;

        return sendText(arreglo, "registrarActivo");

    }
    public String modificarActivo(String usuario,String id, String producto, String Descripcion, String empresa, String departamento) {
        String arreglo = usuario + "$" + id + "$" + producto + "$" + Descripcion + "$" + empresa + "$" + departamento;

        return sendText(arreglo, "modificaractivo");

    }

    public String GenerarID() {
        String id = sendText("", "generarid");
        return id;
    }

    public String EliminarUsuario(String usuario, String empresa, String departamento) {
        String arreglo = usuario + "$" + empresa + "$" + departamento;
        sendText(arreglo, "eliminarUsuario");
        return "Eliminado";
    }

    
    public String rentarActivo(String usuario, String empresa, String departamento, String idActivo){
        String arreglo = usuario +"$" +empresa +"$" +departamento +"$" +idActivo;
        sendText(arreglo, "rentarActivo");
        return "Rentado";
    }
    public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
        } catch (Exception ex) {
        }
        return null;
    }

    public static String sendText(String informacion, String tipo) {

        RequestBody formBody = new FormEncodingBuilder()
                .add("tipo", tipo)
                .add("informacion", informacion)
                .build();
        String r = getString("Matriz", formBody);
        return r;
    }

    public static String sendText(String usuario, String empresa, String departamento, String tipo) {

        RequestBody formBody = new FormEncodingBuilder()
                .add("tipo", tipo)
                .add("usuario", usuario)
                .add("empresa", empresa)
                .add("departamento", departamento)
                .build();
        String r = getString("Matriz", formBody);
        return r;
    }

    public static String sendText(String usuario, String empresa, String departamento, String id, String tipo) {

        RequestBody formBody = new FormEncodingBuilder()
                .add("tipo", tipo)
                .add("usuario", usuario)
                .add("empresa", empresa)
                .add("departamento", departamento)
                .add("id", id)
                .build();
        String r = getString("Matriz", formBody);
        return r;
    }

}
