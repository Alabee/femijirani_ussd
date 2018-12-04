package com.example.whambuoy.jirani;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    Button login;
    EditText name;
    EditText pass;
    ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        listView = (ListView) findViewById(R.id.listView);
        getAgentDetails();

        name = (EditText) findViewById(R.id.username);
        pass = (EditText) findViewById(R.id.password);
        login = (Button) findViewById(R.id.login);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                validateCredentials();
            }
        });
    }

    public void validateCredentials(){
        Toast.makeText(this, "Good!", Toast.LENGTH_SHORT).show();
    }

    public void getAgentDetails(){
        //Create Retrofit object
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(Api.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        Api api = retrofit.create(Api.class);

        Call<List<Agents>> call = api.getAgents();

        call.enqueue(new Callback<List<Agents>>() {
            @Override
            public void onResponse(Call<List<Agents>> call, Response<List<Agents>> response) {

                List<Agents> agents = response.body();

                //Display names of the agents in listview
                String[] agentNames = new String[agents.size()];
                for (int i = 0; i<agents.size(); i++){
                    agentNames[i] = agents.get(i).getUsername();
                }
                listView.setAdapter(
                        new ArrayAdapter<String>(
                                getApplicationContext(),
                                android.R.layout.simple_list_item_1,
                                agentNames
                        )
                );
                /*for(Agents a: agents){
                    Log.d("id", a.getId());
                    Log.d("username", a.getUsername());
                    Log.d("password", a.getPassword());
                    Log.d("agent", a.getAgent());
                }
                */
            }

            @Override
            public void onFailure(Call<List<Agents>> call, Throwable t) {

                Toast.makeText(getApplicationContext(), t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });

    }
}
