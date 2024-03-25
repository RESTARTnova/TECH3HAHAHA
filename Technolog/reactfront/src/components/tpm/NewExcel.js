import ExcelJS from 'exceljs'
import './NewExcelStyle.scss'

// style:{fill: {type: 'pattern',pattern: 'solid',fgColor:{argb:'a8ff0000'}}} ff55d4ed

export const Test = ({pres,name1}) => {
    const yes = (pres,name1) =>{
        const fileType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8";
        const workBook = new ExcelJS.Workbook();
        const sheet1 = workBook.addWorksheet('Страница 1');
        var nomer = 0;
        const re = [{header:'№ п/п',key:'pp'},{header:'Должность',key:'job'},{header:'Начало обхода',key:'start_time'},{header:'Конец обхода',key:'stop_time'},{header:'Комнаты',key:'name'},{header:'Действие',key:'remarks'},{header:'Замечание',key:'note'}];
        sheet1.columns = re;
        pres.forEach(e => {
            // sheet1.addRow({login:e.login,job:e.job,start_time:e.start_time,stop_time:e.stop_time,name:'-',remarks:'-',note:'-'}).eachCell(cell=>{
            //     cell.fill={
            //         type: 'pattern',
            //         pattern:'solid',
            //         fgColor: {
            //             argb: 'ff55d4ed'
            //         }
            //     }
            //     cell.border={
            //         top:{style: 'thin'},
            //         right:{style: 'thin'},
            //         bottom:{style: 'thin'},
            //         left:{style: 'thin'}
            //     }
            // });
            e.rooms.forEach(u=>{
                // sheet1.addRow({login:'-',job:'-',start_time:'-',stop_time:'-',name:u.name,remarks:'-',note:'-'}).eachCell(e=>{
                //     e.fill={
                //         type:'pattern',
                //         pattern:'solid',
                //         fgColor:{
                //             argb:'ff5b86f5'
                //         }
                //     };
                //     e.border={
                //         top:{style: 'thin'},
                //         right:{style: 'thin'},
                //         bottom:{style: 'thin'},
                //         left:{style: 'thin'}
                //     }
                // });
                // sheet1.addRow({login:e.login,job:e.job,start_time:e.start_time,stop_time:e.stop_time,name:u.name});
                u.remarks.forEach(o=>{
                    // sheet1.addRow({login:'-',job:'-',start_time:'-',stop_time:'-',name:'-',remarks:o.name,note:o.note}).eachCell(e=>{
                    //     e.fill={
                    //         type:'pattern',
                    //         pattern:'solid',
                    //         fgColor: {
                    //             argb: 'ff8c69f5'
                    //         }
                    //     };
                    //     e.border={
                    //         top:{style: 'thin'},
                    //         right:{style: 'thin'},
                    //         bottom:{style: 'thin'},
                    //         left:{style: 'thin'}
                    //     }
                    // });
                    sheet1.addRow({pp:nomer,job:e.job,start_time:e.start_time,stop_time:e.stop_time,name:u.name,remarks:o.name,note:o.note});
                    nomer++;
                })
            })
        });
        const numberColumn = sheet1.getColumn(1);
        const jobColumn = sheet1.getColumn(2);
        const startColumn = sheet1.getColumn(3);
        const stopColumn = sheet1.getColumn(4);
        const nameColumn = sheet1.getColumn(5);
        const remarkColumn = sheet1.getColumn(6);
        const noteColumn = sheet1.getColumn(7);
        numberColumn.eachCell(cell=>{
            cell.fill = {
                type: 'pattern',
                pattern: 'solid',
                fgColor: {
                    argb: '0087d7e0'
                }
            };
            cell.border={
                top:{style: 'thin'},
                right:{style: 'thin'},
                bottom:{style: 'thin'},
                left:{style: 'thin'}
            }
        });
        jobColumn.eachCell(cell=>{
            cell.fill = {
                type: 'pattern',
                pattern: 'solid',
                fgColor: {
                    argb: '00fa2542'
                }
            };
            cell.border={
                top:{style: 'thin'},
                right:{style: 'thin'},
                bottom:{style: 'thin'},
                left:{style: 'thin'}
            }
        });
        startColumn.eachCell(cell=>{
            cell.fill = {
                type: 'pattern',
                pattern: 'solid',
                fgColor: {
                    argb: '005fd980'
                }
            };
            cell.border={
                top:{style: 'thin'},
                right:{style: 'thin'},
                bottom:{style: 'thin'},
                left:{style: 'thin'}
            }
        });
        stopColumn.eachCell(cell=>{
            cell.fill = {
                type: 'pattern',
                pattern: 'solid',
                fgColor: {
                    argb: '005fd980'
                }
            };
            cell.border={
                top:{style: 'thin'},
                right:{style: 'thin'},
                bottom:{style: 'thin'},
                left:{style: 'thin'}
            }
        });
        nameColumn.eachCell(cell=>{
            cell.fill = {
                type: 'pattern',
                pattern: 'solid',
                fgColor: {
                    argb: '00e0ed51'
                }
            };
            cell.border={
                top:{style: 'thin'},
                right:{style: 'thin'},
                bottom:{style: 'thin'},
                left:{style: 'thin'}
            }
        });
        remarkColumn.eachCell(cell=>{
            cell.fill = {
                type: 'pattern',
                pattern: 'solid',
                fgColor: {
                    argb: '00be9ede'
                }
            };
            cell.border={
                top:{style: 'thin'},
                right:{style: 'thin'},
                bottom:{style: 'thin'},
                left:{style: 'thin'}
            }
        });
        noteColumn.eachCell(cell=>{
            cell.fill = {
                type: 'pattern',
                pattern: 'solid',
                fgColor: {
                    argb: '009f6dd1'
                }
            };
            cell.border={
                top:{style: 'thin'},
                right:{style: 'thin'},
                bottom:{style: 'thin'},
                left:{style: 'thin'}
            }
        });
        re.forEach(({header,key})=>{
            var maxLen = 0;
            sheet1.getColumn(key).eachCell(({includeEmpty: true},cell=>{
                const cellValue = cell.text || '';
                maxLen = Math.max(maxLen,cellValue.length);
            }))
            const headerText = header.toUpperCase();
            const colemn = sheet1.getColumn(key);
            colemn.width = maxLen < 20 ? 20 : maxLen + 10;
            colemn.header = headerText;
        });
        const headerRpw = sheet1.getRow(1);
        headerRpw.eachCell(cell=>{
            cell.fill = {
                type: 'pattern',
                pattern: 'solid',
                fgColor: {
                    argb: '005df076'
                }
            };
            cell.border={
                top:{style: 'thin'},
                right:{style: 'thin'},
                bottom:{style: 'thin'},
                left:{style: 'thin'}
            }
        })
        workBook.xlsx.writeBuffer().then(succs=>{
            var a = succs;
            const blob = new Blob([a],{type: fileType});
            const url = URL.createObjectURL(blob);
            const a1 = document.createElement('a');
            a1.href = url;
            a1.download = name1 + '.xlsx';
            a1.click();
        });
    }

    return(
        <button onClick={()=>{yes(pres,name1)}} className='excelButton'>Вывести в Excel</button>
    )
}