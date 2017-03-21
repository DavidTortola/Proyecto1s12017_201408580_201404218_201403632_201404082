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
import java.util.logging.Level;

/**
 *
 * @author Andree
 */
public class Flask {

    public static OkHttpClient webClient = new OkHttpClient();

    public Flask() {

    }

    public String Login(String user, String pass, String empresa, String departamento) {
        //Metodo para buscar en la matriz

        return sendText(user, "buscar");
    }

    public String Registrar(String user, String pass,String nombre, String empresa, String departamento) {
        String arreglo = user+"$"+pass+"$"+nombre+"$"+empresa+"$"+departamento;
        return sendText(arreglo,"registrar");

    }
    public String RegistrarActivo(String usuario,String id,String producto,String Descripcion){
    String arreglo = usuario+"$"+id+"$"+producto+"$"+Descripcion;

    return sendText(arreglo,"registrarActivo");
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

}
