import {
  Flex,
  Text,
  Button,
  Box,
  Card,
  CardHeader,
  CardBody,
  Heading,
  Popover,
  PopoverTrigger,
  PopoverArrow,
  PopoverContent,
  PopoverCloseButton,
  PopoverBody,
} from "@chakra-ui/react";

import { Link } from "react-router-dom";

export default function CardView({
  index,
  name,
  manufacturer,
  barcode,
  price,
  total_quantity,
  booked_quantity,
  description,
}) {
  return (
    <Flex
      bg="white"
      flexDirection="column"
      alignItems="center"
      rounded="md"
      mr={10}
      ml={10}
      p={6}
      mt={10}
      maxWidth={360}
    >
      <Card bg="gray.100" p={4} roundedTop="md" mb={4}>
        <CardHeader>
          <Heading size="lg">{name}</Heading>
        </CardHeader>
        <CardBody>
          <Text size="md">Производитель</Text>
          <Heading size="md" mb={1}>
            {manufacturer}
          </Heading>
          <Text size="md">Штрих-код</Text>
          <Heading size="md" mb={1}>
            {barcode}
          </Heading>
          <Text size="md">Цена</Text>
          <Heading size="md" mb={1}>
            {price}
          </Heading>
          <Text size="md">Количество</Text>
          <Heading size="md" mb={1}>
            {total_quantity}
          </Heading>
          <Text size="md">Забронировано</Text>
          <Heading size="md" mb={1}>
            {booked_quantity}
          </Heading>
          <Popover>
            <PopoverTrigger>
              <Button
                m={0}
                p={0}
                b={0}
                size="md"
                outline="none"
                colorScheme="teal"
                variant="link"
              >
                Описание
              </Button>
            </PopoverTrigger>
            <PopoverContent>
              <PopoverArrow />
              <PopoverCloseButton />
              <PopoverBody p={5}>{description}</PopoverBody>
            </PopoverContent>
          </Popover>
        </CardBody>
      </Card>

      <Flex maxWidth={360} w="100%">
        <Link to={"/product_update"} className="link" style={{ width: "100%" }}>
          <Button colorScheme="teal" w="full">
            Изменить
          </Button>
        </Link>
        <Button colorScheme="teal" ml={2}>
          X
        </Button>
      </Flex>
    </Flex>
  );
}
