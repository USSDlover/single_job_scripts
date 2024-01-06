const getPos = require('./cursor-pos');

const AppMain = async function () {
    process.stdout.write('HELLO 123');
    const test = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,10];
    for (let d of test) {
        const pos = await getPos();
        process.stdout.cursorTo(0, Number(pos.rows) - 1);
        process.stdout.clearLine(0);
        process.stdout.cursorTo(0, Number(pos.rows) - 2);
        process.stdout.clearLine(0);
        console.log(d, { pos });
    }
}

AppMain();
