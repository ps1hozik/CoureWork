/* eslint-disable react/prop-types */
import { Flex, Button, Select } from "@chakra-ui/react";

import { Link } from "react-router-dom";

import CardView from "./card_view";
import TableView from "./table_view";

import React, { useState, useEffect } from "react";
import Cookies from "universal-cookie";

const Head = ({
  setViewB,
  manufacturers,
  setManufacturers,
  w_id,
  setProducts,
}) => {
  const filter_product = (e) => {
    var manufacturer = e.target.value;
    if (!manufacturer) {
      manufacturer = "all";
    }
    console.log(manufacturer);
    fetch(
      `http://localhost:8000/product/${w_id}/get_by_manufacturer/${manufacturer}`,
      {
        method: "GET",
        headers: { "Content-Type": "application/json" },
      }
    )
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        console.log(data);
        if (data.status === "success") {
          setProducts(data.data.products);
          setManufacturers(data.data.manufacturers);
        }
      })
      .catch(function (error) {
        console.log(error, "error");
      });
  };

  const [view, setView] = useState("Вид: Таблица");

  const handleChangeView = () => {
    if (view === "Вид: Таблица") {
      setView("Вид: Карточки");
      setViewB(false);
    } else {
      setView("Вид: Таблица");
      setViewB(true);
    }
  };
  return (
    <Flex
      bg="gray.50"
      justify="space-between"
      gap={30}
      pl={10}
      pr={10}
      zIndex={1}
      width="100%"
    >
      <Link to={"/product_add"} style={{ margin: 4, width: "100%" }}>
        <Button colorScheme="teal" w="100%">
          Добавить
        </Button>
      </Link>
      <Link to={"/warehouse_get"} style={{ margin: 4, width: "100%" }}>
        <Button
          colorScheme="teal"
          w="100%"
          onClick={() => {
            na;
          }}
        >
          Склады
        </Button>
      </Link>
      <Select
        placeholder="Все"
        colorScheme="teal"
        variant="filled"
        w="50%"
        p={1}
        minWidth={120}
        onChange={filter_product}
      >
        {manufacturers.map((manufacturer, i) => (
          <option key={i} value={manufacturer}>
            {manufacturer}
          </option>
        ))}
      </Select>
      <Button
        colorScheme="teal"
        m={1}
        onClick={handleChangeView}
        w="30%"
        minWidth={120}
        p={4}
      >
        {view}
      </Button>
    </Flex>
  );
};

export default function ProductList() {
  const [products, setProducts] = useState([]);
  const [manufacturers, setManufacturers] = useState([]);
  const cookies = new Cookies();

  const w_id = cookies.get("warehouse_id");
  const deleteProduct = () => {
    const p_id = cookies.get("product_id");

    fetch(`http://localhost:8000/product/${w_id}/${p_id}`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
    })
      .then(function () {
        console.log("remove success");
      })
      .catch(function (error) {
        console.log(error, "error");
      });
    setProducts((prev) => [...prev].filter((el) => el.id !== p_id));
    cookies.remove("product_id");
  };

  useEffect(() => {});

  useEffect(() => {
    fetch(`http://localhost:8000/product/${w_id}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        if (data.status === "success") {
          console.log(data.data.products);
          setProducts(data.data.products);
          setManufacturers(data.data.manufacturers);
        }
      })
      .catch(function (error) {
        console.log(error, "error");
      });
  }, [w_id]);

  const [viewB, setViewB] = useState(true);

  const View = () => {
    if (!viewB) {
      return <TableView products={products} />;
    } else {
      return (
        <>
          {products.map((product) => (
            <CardView
              key={product.id}
              id={product.id}
              name={product.name}
              manufacturer={product.manufacturer}
              barcode={product.barcode}
              price={product.price}
              total_quantity={product.total_quantity}
              booked_quantity={product.booked_quantity}
              description={product.description}
              remove={deleteProduct}
            />
          ))}
        </>
      );
    }
  };

  return (
    <>
      <Head
        setViewB={setViewB}
        w_id={w_id}
        setProducts={setProducts}
        manufacturers={manufacturers}
        setManufacturers={setManufacturers}
      />
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
