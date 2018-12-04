package com.example.whambuoy.jirani;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;

public interface Api {
    String BASE_URL = "http://10.1.0.10:8000/data/";

    @GET("agent")
    Call<List<Agents>> getAgents();
}
