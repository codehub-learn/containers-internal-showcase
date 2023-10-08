package gr.codehub.simpleproject.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MainController {

    @GetMapping("/")
    public String index(){
        return "Wow! I am running perfectly! :O";
    }
}
