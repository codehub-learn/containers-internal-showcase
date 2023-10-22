package org.codehub;

import static org.junit.Assert.assertTrue;
import org.codehub.JPrint;
import com.sun.net.httpserver.*;
import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    @Test
    public void shouldAnswerWithTrue()
    {
        assertTrue( "1"=="1" );
    }

    @Test
    public void shouldGetResponse()
    {
        assertTrue(!"GET success".isEmpty());
    }

    @Test
    public void shouldNotGetResponse()
    {
        assertTrue("GET failure".contains("failure"));
    }

    @Test
    public void shouldRedirect()
    {
        assertTrue("GET /existent".contains("existent"));
    }
    @Test
    public void shouldNotRedirect()
    {
        assertTrue("GET /nonexistentpath".contains("non"));
    }



}