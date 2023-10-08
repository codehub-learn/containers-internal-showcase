package gr.codehub.simpleproject;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.assertEquals;

@ExtendWith(MockitoExtension.class)
@SpringBootTest(classes = SimpleServiceTest.class)
class SimpleServiceTest {

	@Test
	@DisplayName("First Test")
	void insertItem() {
		int number = 1;
		assertEquals(number, 1);
	}
}
