/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package WebService;

import Logica.Flask;
import Logica.WebService1;
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
        return (new Flask().Login(parameter, parameter, parameter, parameter)).toString();
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
     * @param user
     * @param pass
     * @param empresa
     * @param departamento
     * @return 
     */
    @WebMethod(operationName = "Login")
    public String Login(@WebParam(name = "user") String user, @WebParam(name = "pass") String pass, @WebParam(name = "empresa") String empresa, @WebParam(name = "departamento") String departamento) {
        //TODO write your implementation code here:
        return (new Flask().Login(user, pass, empresa, departamento));
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "insertarAB")
    public String insertarAB(@WebParam(name = "id") String id, @WebParam(name = "idactivo") String idactivo, @WebParam(name = "usuario") String usuario, @WebParam(name = "empresa") String empresa, @WebParam(name = "departamento") String departamento, @WebParam(name = "fecha") String fecha, @WebParam(name = "tiempo") String tiempo) {
        //TODO write your implementation code here:
        return (new WebService1().getWebService1Soap().insertar(id, idactivo, usuario, empresa, departamento, fecha, tiempo));
    }
    
    
    
}
