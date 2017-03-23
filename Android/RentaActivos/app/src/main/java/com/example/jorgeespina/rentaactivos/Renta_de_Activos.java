package com.example.jorgeespina.rentaactivos;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

/**
 * Created by Jorge Espina on 14/03/2017.
 */

public class Renta_de_Activos extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.rentadeactivos);
       /* Button boton = (Button) findViewById(R.id.btnrentar);
        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                //Intent nuevoform = new Intent(Renta_de_Activos.this,Secundaria.class);
                //startActivity(nuevoform);
            }
        });*/
        Button boton1 = (Button) findViewById(R.id.btnregresarmenu);
        boton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                Intent nuevoform = new Intent(Renta_de_Activos.this,Secundaria.class);
                startActivity(nuevoform);
            }
        });

    }
}
