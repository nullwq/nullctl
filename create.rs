use std::process::Command;
use tokio; //shit i dont know
fn create_dock(&mut name: val: string, &mut cpu:val :string, &mut mem:val:string) -> Result<(), String> {
    let output = Command::new("docker")
        .arg(&["container","create","--name", &name,"--cpus", &cpu,"--user","1000:1000","--memory", &mem,"-it","ubuntu:latest","/bin/bash"])
        .output();
        .status();
        .expect("Oh shoot! Exception occured while creating the cell! please try again");
    if output.success() {
        Ok(())
    } else {
        Err(String::from("Something went wrong while trying to create an cell please try again"))
    }

}
fn name_generator(len: usize){
      let charset = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ\
                    abcdefghijklmnopqrstuvwxyz\
                    0123456789";
    let mut rng = thread_rng();
    (0..len)
        .map(|_| {
            let idx = rng.gen_range(0..charset.len());
            charset[idx] as char
        })
        .collect()
}
fn main(){
    try{
        let cpu: Vec<String> = env::args().nth(0).except("Error occured: No arguments passed to CPU")
        let mem: Vec<String> = env::args().nth(1).except("Error occured: No arguments passed to MEMORY");
        create_dock(name_generator(32), cpu, mem);
    }catch(e){
        println!("Error occured: {}", e);
    }
}