import {element} from './client.js';

function block(target,className,content) {
  const node=element('div',content,{class:className});
  target.append(node);
  return node;
}
const note=(target,text)=>block(target,'chart-note',text);

export function visualize(report,selected) {
  const target=document.querySelector('#visual');
  target.replaceChildren();
  const measurement=report.cases?.find(row=>row.case===selected)?.measure;
  if (!measurement) {block(target,'chart-note','选择有计算值的分组');return;}
  const e=measurement.evidence;

  const line=block(target,'bus-route');
  for(const [index,station] of e.route.entries()) {
    const item=block(line,'route-node'); block(item,'route-disc',String(index+1));
    block(item,'legend',`${station} 站`); block(item,'route-ping',e.pings[index]);
  }
  if (e.missing.length) note(target,`缺站 ${e.missing.join('、')}`);
}
