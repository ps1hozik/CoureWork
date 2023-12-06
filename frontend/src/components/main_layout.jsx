import { Link } from "react-router-dom";
import { Box, Button } from "@chakra-ui/react";

const MainLayout = ({ children }) => {
  return (
    <Box>
      {children}
      <Box position="fixed" bottom={4} left={4}>
        <Link to="/">
          <Button colorScheme="teal" opacity={0.6}>
            На главную
          </Button>
        </Link>
      </Box>
    </Box>
  );
};

export default MainLayout;
