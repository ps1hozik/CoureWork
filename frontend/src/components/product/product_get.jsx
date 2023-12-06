/* eslint-disable react/prop-types */
import { Flex, Button, Tr } from "@chakra-ui/react";

import { Link } from "react-router-dom";

import CardView from "./card_view";
import TableView from "./table_view";

import React, { useState } from "react";

const Head = ({ viewB, setViewB }) => {
  const [view, setView] = useState("Вид: Карточки");

  const handleChangeView = () => {
    if (view === "Вид: Карточки") {
      setView("Вид: Таблица");
      setViewB(false);
    } else {
      setView("Вид: Карточки");
      setViewB(true);
    }
  };
  return (
    <Flex
      position="fixed"
      bg="gray.50"
      justify="center"
      gap={30}
      pl={20}
      pr={20}
      zIndex={1}
      width="100%"
    >
      <Link
        to={"/product_add"}
        className="link"
        style={{ margin: 4, marginRight: 10, width: "100%" }}
      >
        <Button colorScheme="teal" w="100%">
          Добавить
        </Button>
      </Link>
      <Link
        to={"/warehouse_get"}
        className="link"
        style={{ margin: 4, marginLeft: 10, width: "100%" }}
      >
        <Button colorScheme="teal" w="100%">
          Склады
        </Button>
      </Link>
      <Button
        colorScheme="teal"
        m={1}
        ml={4}
        w="20%"
        onClick={handleChangeView}
      >
        {view}
      </Button>
    </Flex>
  );
};

export default function WarehouseList() {
  const products = [
    {
      name: "Сырок творожный1",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный2",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный3",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный4",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный5",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный6",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный7",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный8",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный9",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный10",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный11",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный12",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
    {
      name: "Сырок творожный13",
      manufacturer: "Савушкин продукт",
      barcode: "103102030481",
      price: "0.75",
      total_quantity: "100000",
      booked_quantity: "7800",
      description:
        "Условия и сроки хранения хранить при t (4±2) °С. Дата изготовления и срок годности указаны на упаковке.",
    },
  ];
  const [viewB, setViewB] = useState(true);

  const View = () => {
    if (viewB) {
      return <TableView products={products} />;
    } else {
      return (
        <>
          {products.map((product, index) => (
            <CardView
              key={index}
              index={index}
              name={product.name}
              manufacturer={product.manufacturer}
              barcode={product.barcode}
              price={product.price}
              total_quantity={product.total_quantity}
              booked_quantity={product.booked_quantity}
              description={product.description}
            />
          ))}
        </>
      );
    }
  };

  return (
    <>
      <Head viewB={viewB} setViewB={setViewB} />
      <Flex
        bg="gray.100"
        align="center"
        justify="center"
        flexWrap="wrap"
        overflow="auto"
        p={6}
      >
        <View />
      </Flex>
    </>
  );
}
