/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package WebService;

import Logica.Flask;
import Logica.WebService1;
import java.util.Date;
import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

/**
 *
 * @author Andree
 */
@WebService(serviceName = "Principal")
public class Principal {

    /**
     * This is a sample web service operation
     */
    @WebMethod(operationName = "hello")
    public String hello(@WebParam(name = "name") String txt) {
        return (new WebService1().getWebService1Soap()).prueba(txt);
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "Prueba")
    public String Prueba(@WebParam(name = "parameter") String parameter) {
        //TODO write your implementation code here:       
        //return (new Flask().Login(parameter, parameter, parameter, parameter)).toString();
        return null;
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "Registrar")
    public String Registrar(@WebParam(name = "usuario") String usuario, @WebParam(name = "pass") String pass, @WebParam(name = "nombre") String nombre, @WebParam(name = "departamento") String departamento, @WebParam(name = "empresa") String empresa) {
        //TODO write your implementation code here:
        return (new Flask().Registrar(usuario, pass, nombre, empresa, departamento));
    }

    /**
     * Web service operation
     *
     * @param user
     * @param pass
     * @param empresa
     * @param departamento
     * @return
     */
    @WebMethod(operationName = "Login")
    public boolean Login(@WebParam(name = "user") String user, @WebParam(name = "pass") String pass, @WebParam(name = "empresa") String empresa, @WebParam(name = "departamento") String departamento) {
        //TODO write your implementation code here:
        return (new Flask().Login(user, pass, empresa, departamento));
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "InsertarAB")
    public String InsertarAB(@WebParam(name = "idActivo") String idActivo, @WebParam(name = "usuario") String usuario, @WebParam(name = "empresa") String empresa, @WebParam(name = "departamento") String departamento, @WebParam(name = "tiempo") String tiempo) {
        //TODO write your implementation code here:
        Date date = new Date();
        String id = (new Flask().GenerarID());
        String fecha = date.toString();
        String gg = (new WebService1().getWebService1Soap().insertar(id, idActivo, usuario, empresa, departamento, fecha, tiempo));
        return "Identificador de Renta: " + id + "  " + gg;
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "RegistrarActivo")
    public String RegistrarActivo(@WebParam(name = "usuario") String usuario, @WebParam(name = "nombreProducto") String nombreProducto, @WebParam(name = "descripcion") String descripcion, @WebParam(name = "empresa") String empresa, @WebParam(name = "departamento") String departamento) {
        //TODO write your implementation code here:
        return (new Flask().RegistrarActivo(usuario, nombreProducto, descripcion, empresa, departamento));
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "EliminarTransaccion")
    public String EliminarTransaccion(@WebParam(name = "idActivo") String idActivo) {
        //TODO write your implementation code here:
        return (new WebService1().getWebService1Soap().eliminar(idActivo));
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "ObtenerIdArbol")
    public String[] ObtenerIdArbol(@WebParam(name = "usuario") String usuario, @WebParam(name = "empresa") String empresa, @WebParam(name = "departamento") String departamento) {
        //TODO write your implementation code here:
        String[] valores = new Flask().obtenerIdArbol(usuario, empresa, departamento);
        return valores;
        
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "ModificarActivo")
    public String ModificarActivo(@WebParam(name = "usuario") String usuario, @WebParam(name = "id") String id, @WebParam(name = "producto") String producto, @WebParam(name = "descripcion") String descripcion, @WebParam(name = "empresa") String empresa, @WebParam(name = "departamento") String departamento) {
        //TODO write your implementation code here:
        return (new Flask().modificarActivo(usuario, id, producto, descripcion, empresa, departamento));
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "EliminarActivo")
    public String EliminarActivo(@WebParam(name = "usuario") String usuario, @WebParam(name = "id") String id, @WebParam(name = "empresa") String empresa, @WebParam(name = "deartamento") String deartamento) {
        //TODO write your implementation code here:
        return new Flask().EliminarActivo(usuario, empresa, deartamento, id);
    }
    
}
