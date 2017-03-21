/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package WebService;

import Logica.Flask;
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
        return "Hello " + txt + " !";
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
    
    
    
}
