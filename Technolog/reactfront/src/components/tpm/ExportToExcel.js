import React from 'react'
import * as FileSaver from "file-saver";
import * as XLSX from "xlsx";

export const ExportToExcel = ({ apiData, fileName }) => {
  const fileType =
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8";
  const fileExtension = ".xlsx";

  const exportToCSV = (apiData, fileName) => {
    const wb = XLSX.utils.book_new();
    const ws = XLSX.utils.aoa_to_sheet(apiData);
    const wb1 = { Sheets: { data: ws }, SheetNames: ["data"] };
    const excelBuffer = XLSX.write(wb1, { bookType: "xlsx", type: "array" });
    const data = new Blob([excelBuffer], { type: fileType });
    FileSaver.saveAs(data, fileName + fileExtension);
  };

  return (
    <button onClick={(e) => exportToCSV(apiData, fileName)}>Экспортировать в Excel формате</button>
  );
};