package com.example.jorgeespina.rentaactivos;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

/**
 * Created by Jorge Espina on 14/03/2017.
 */

public class Registro_de_Devoluciones extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.registrodedevoluciones);
        Button boton1 = (Button) findViewById(R.id.btnregresar);
        boton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                Intent nuevoform = new Intent(Registro_de_Devoluciones.this,Secundaria.class);
                startActivity(nuevoform);
            }
        });
        Button boton = (Button) findViewById(R.id.btnmenuregresar);
        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                Intent nuevoform = new Intent(Registro_de_Devoluciones.this,Secundaria.class);
                startActivity(nuevoform);
            }
        });

    }
}