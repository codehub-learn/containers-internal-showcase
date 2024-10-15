package org.codehub;

import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpRetryException;
import java.net.InetSocketAddress;
import com.sun.net.httpserver.*;


class JPrint {
    public static void main(String[] args) throws IOException{
        HttpServer server = HttpServer.create(new InetSocketAddress(8900), 0);
        HttpContext context = server.createContext("/");
        context.setHandler(JPrint::handleGet);
        server.start();
    }

    private static void handleGet(HttpExchange exchange) throws IOException {
        String response = "Hello from Pfizer again";
        exchange.sendResponseHeaders(200, response.getBytes().length);
        OutputStream os = exchange.getResponseBody();
        os.write(response.getBytes());
        os.close();
    }

}