
package Logica;

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebResult;
import javax.jws.WebService;
import javax.xml.bind.annotation.XmlSeeAlso;
import javax.xml.ws.RequestWrapper;
import javax.xml.ws.ResponseWrapper;


/**
 * This class was generated by the JAX-WS RI.
 * JAX-WS RI 2.2.11-b150120.1832
 * Generated source version: 2.2
 * 
 */
@WebService(name = "WebService1Soap", targetNamespace = "http://tempuri.org/")
@XmlSeeAlso({
    ObjectFactory.class
})
public interface WebService1Soap {


    /**
     * 
     * @return
     *     returns java.lang.String
     */
    @WebMethod(operationName = "HelloWorld", action = "http://tempuri.org/HelloWorld")
    @WebResult(name = "HelloWorldResult", targetNamespace = "http://tempuri.org/")
    @RequestWrapper(localName = "HelloWorld", targetNamespace = "http://tempuri.org/", className = "Logica.HelloWorld")
    @ResponseWrapper(localName = "HelloWorldResponse", targetNamespace = "http://tempuri.org/", className = "Logica.HelloWorldResponse")
    public String helloWorld();

    /**
     * 
     * @param par
     * @return
     *     returns java.lang.String
     */
    @WebMethod(operationName = "Prueba", action = "http://tempuri.org/Prueba")
    @WebResult(name = "PruebaResult", targetNamespace = "http://tempuri.org/")
    @RequestWrapper(localName = "Prueba", targetNamespace = "http://tempuri.org/", className = "Logica.Prueba")
    @ResponseWrapper(localName = "PruebaResponse", targetNamespace = "http://tempuri.org/", className = "Logica.PruebaResponse")
    public String prueba(
        @WebParam(name = "par", targetNamespace = "http://tempuri.org/")
        String par);

    /**
     * 
     * @param descripcion
     * @param idactivo
     * @param fecha
     * @param idrenta
     * @param tiempo
     * @param departamento
     * @param empresa
     * @param nombre
     * @param user
     * @return
     *     returns java.lang.String
     */
    @WebMethod(action = "http://tempuri.org/insertar")
    @WebResult(name = "insertarResult", targetNamespace = "http://tempuri.org/")
    @RequestWrapper(localName = "insertar", targetNamespace = "http://tempuri.org/", className = "Logica.Insertar")
    @ResponseWrapper(localName = "insertarResponse", targetNamespace = "http://tempuri.org/", className = "Logica.InsertarResponse")
    public String insertar(
        @WebParam(name = "idrenta", targetNamespace = "http://tempuri.org/")
        String idrenta,
        @WebParam(name = "idactivo", targetNamespace = "http://tempuri.org/")
        String idactivo,
        @WebParam(name = "nombre", targetNamespace = "http://tempuri.org/")
        String nombre,
        @WebParam(name = "descripcion", targetNamespace = "http://tempuri.org/")
        String descripcion,
        @WebParam(name = "user", targetNamespace = "http://tempuri.org/")
        String user,
        @WebParam(name = "empresa", targetNamespace = "http://tempuri.org/")
        String empresa,
        @WebParam(name = "departamento", targetNamespace = "http://tempuri.org/")
        String departamento,
        @WebParam(name = "fecha", targetNamespace = "http://tempuri.org/")
        String fecha,
        @WebParam(name = "tiempo", targetNamespace = "http://tempuri.org/")
        String tiempo);

    /**
     * 
     * @param idActivo
     * @return
     *     returns java.lang.String
     */
    @WebMethod(action = "http://tempuri.org/eliminar")
    @WebResult(name = "eliminarResult", targetNamespace = "http://tempuri.org/")
    @RequestWrapper(localName = "eliminar", targetNamespace = "http://tempuri.org/", className = "Logica.Eliminar")
    @ResponseWrapper(localName = "eliminarResponse", targetNamespace = "http://tempuri.org/", className = "Logica.EliminarResponse")
    public String eliminar(
        @WebParam(name = "idActivo", targetNamespace = "http://tempuri.org/")
        String idActivo);

    /**
     * 
     * @param departamento
     * @param usuario
     * @param empresa
     * @return
     *     returns Logica.ArrayOfString
     */
    @WebMethod(action = "http://tempuri.org/getActivos")
    @WebResult(name = "getActivosResult", targetNamespace = "http://tempuri.org/")
    @RequestWrapper(localName = "getActivos", targetNamespace = "http://tempuri.org/", className = "Logica.GetActivos")
    @ResponseWrapper(localName = "getActivosResponse", targetNamespace = "http://tempuri.org/", className = "Logica.GetActivosResponse")
    public ArrayOfString getActivos(
        @WebParam(name = "usuario", targetNamespace = "http://tempuri.org/")
        String usuario,
        @WebParam(name = "empresa", targetNamespace = "http://tempuri.org/")
        String empresa,
        @WebParam(name = "departamento", targetNamespace = "http://tempuri.org/")
        String departamento);

    /**
     * 
     * @param idActivo
     */
    @WebMethod(action = "http://tempuri.org/regresarActivo")
    @RequestWrapper(localName = "regresarActivo", targetNamespace = "http://tempuri.org/", className = "Logica.RegresarActivo")
    @ResponseWrapper(localName = "regresarActivoResponse", targetNamespace = "http://tempuri.org/", className = "Logica.RegresarActivoResponse")
    public void regresarActivo(
        @WebParam(name = "idActivo", targetNamespace = "http://tempuri.org/")
        String idActivo);

}
