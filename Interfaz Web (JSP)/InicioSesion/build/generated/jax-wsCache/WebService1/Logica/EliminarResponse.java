
package Logica;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Clase Java para anonymous complex type.
 * 
 * <p>El siguiente fragmento de esquema especifica el contenido que se espera que haya en esta clase.
 * 
 * <pre>
 * &lt;complexType&gt;
 *   &lt;complexContent&gt;
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType"&gt;
 *       &lt;sequence&gt;
 *         &lt;element name="eliminarResult" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/&gt;
 *       &lt;/sequence&gt;
 *     &lt;/restriction&gt;
 *   &lt;/complexContent&gt;
 * &lt;/complexType&gt;
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "eliminarResult"
})
@XmlRootElement(name = "eliminarResponse")
public class EliminarResponse {

    protected String eliminarResult;

    /**
     * Obtiene el valor de la propiedad eliminarResult.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getEliminarResult() {
        return eliminarResult;
    }

    /**
     * Define el valor de la propiedad eliminarResult.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setEliminarResult(String value) {
        this.eliminarResult = value;
    }

}
