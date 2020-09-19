import lombok.SneakyThrows;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

import java.util.List;

import static java.util.Arrays.asList;

public class ContagemPalavras {

    private static final String JOB_NAME = "contagempalavras";
    private static final Integer INDICE_INPUT = 0;
    private static final Integer INDICE_OUTPUT = 1;

    @SneakyThrows
    public static void main(String[] args) {
        var conf = new Configuration();
        var job = new Job(conf, JOB_NAME);
        configurarJob(job);
        definirInputOutputJob(job, asList(args));
    }

    private static void configurarJob(Job job) {
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        job.setMapperClass(Map.class);
        job.setReducerClass(Reduce.class);
        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);
    }

    @SneakyThrows
    private static void definirInputOutputJob(Job job, List<String> args) {
        System.out.println(args.get(INDICE_INPUT));
        System.out.println(args.get(INDICE_OUTPUT));
        FileInputFormat.addInputPath(job, new Path(args.get(INDICE_INPUT)));
        FileOutputFormat.setOutputPath(job, new Path(args.get(INDICE_OUTPUT)));
        job.waitForCompletion(true);
    }
}
