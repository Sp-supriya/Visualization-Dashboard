import React, { useEffect, useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const Dashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/data")
      .then(response => setData(response.data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  const chartData = {
    labels: data.map(item => item.topic),
    datasets: [
      {
        label: "Intensity",
        data: data.map(item => item.intensity),
        backgroundColor: "rgba(75, 192, 192, 0.6)",
      },
    ],
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold">Data Visualization Dashboard</h1>
      <Card className="mt-4">
        <CardContent>
          <Bar data={chartData} />
        </CardContent>
      </Card>
    </div>
  );
};

export default Dashboard;
